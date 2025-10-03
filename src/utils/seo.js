const DEFAULT_TITLE = '數位學生證｜DID 驗證與校園應用'
const DEFAULT_DESCRIPTION = '使用數位憑證皮夾探索台灣校園的 DID 學生證應用，支援卡證生成、驗證與匿名校園服務。'
const DEFAULT_KEYWORDS = '數位學生證,DID,數位憑證皮夾,台灣,校園,驗證'

const resolveImage = (image) => {
    if (typeof window === 'undefined') return image || '/logo.png'

    if (!image) {
        return `${window.location.origin}/logo.png`
    }

    if (image.startsWith('http')) return image
    if (image.startsWith('/')) return `${window.location.origin}${image}`

    return `${window.location.origin}/${image}`
}

const upsertMeta = ({ key, value, attr }) => {
    if (typeof document === 'undefined' || !value) return

    const selector = attr === 'property'
        ? `meta[property="${key}"]`
        : `meta[name="${key}"]`

    let element = document.head.querySelector(selector)
    if (!element) {
        element = document.createElement('meta')
        element.setAttribute(attr, key)
        document.head.appendChild(element)
    }
    element.setAttribute('content', value)
}

const upsertLink = (rel, href) => {
    if (typeof document === 'undefined' || !href) return

    const selector = `link[rel="${rel}"]`
    let element = document.head.querySelector(selector)
    if (!element) {
        element = document.createElement('link')
        element.setAttribute('rel', rel)
        document.head.appendChild(element)
    }
    element.setAttribute('href', href)
}

export const applySeo = (overrides = {}) => {
    if (typeof document === 'undefined') return

    const {
        title = DEFAULT_TITLE,
        description = DEFAULT_DESCRIPTION,
        keywords = DEFAULT_KEYWORDS,
        ogTitle,
        ogDescription,
        ogImage,
        ogType = 'website',
        canonical
    } = overrides

    const resolvedTitle = ogTitle || title
    const resolvedDescription = ogDescription || description
    const resolvedImage = resolveImage(ogImage)
    const resolvedCanonical = canonical || (typeof window !== 'undefined' ? window.location.href : '')

    document.title = title

    upsertMeta({ key: 'description', value: description, attr: 'name' })
    upsertMeta({ key: 'keywords', value: keywords, attr: 'name' })

    upsertMeta({ key: 'og:title', value: resolvedTitle, attr: 'property' })
    upsertMeta({ key: 'og:description', value: resolvedDescription, attr: 'property' })
    upsertMeta({ key: 'og:type', value: ogType, attr: 'property' })
    upsertMeta({ key: 'og:url', value: resolvedCanonical, attr: 'property' })
    upsertMeta({ key: 'og:image', value: resolvedImage, attr: 'property' })

    upsertMeta({ key: 'twitter:card', value: 'summary_large_image', attr: 'name' })
    upsertMeta({ key: 'twitter:title', value: resolvedTitle, attr: 'name' })
    upsertMeta({ key: 'twitter:description', value: resolvedDescription, attr: 'name' })
    upsertMeta({ key: 'twitter:image', value: resolvedImage, attr: 'name' })

    upsertLink('canonical', resolvedCanonical)
}

export const defaultSeo = {
    title: DEFAULT_TITLE,
    description: DEFAULT_DESCRIPTION,
    keywords: DEFAULT_KEYWORDS,
    ogImage: '/logo.png'
}

