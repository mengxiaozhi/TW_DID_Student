import re
import pandas as pd

raw_data = [
    # 省略，原始data不變
    # 這裡直接貼上原始資料
    {"id":"17","email":"11310226@gm.chihlee.edu.tw","student_id":"11310226","token":"5a94ae959b72eb912b16fc00c0835ae358f127a0","token_expiry":"1744317582971","verified":"0","created_at":"2025-04-04 06:11:30"},
    {"id":"34","email":"11310153@mail.chihlee.edu.tw","student_id":"11310153","token":"1f4847bb971053aec5c28ef8400f99587031237a","token_expiry":"1744021773044","verified":"0","created_at":"2025-04-04 18:29:33"},
    {"id":"37","email":"11310203@gm.chihlee.edu.tw","student_id":"11310203","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-04 19:06:04"},
    {"id":"45","email":"11308107@gm.chihlee.edu.tw","student_id":"11308107","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-04 20:07:43"},
    {"id":"47","email":"11323220@gm.chihlee.edu.tw","student_id":"11323220","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-04 22:43:06"},
    {"id":"48","email":"11202330@gm.chihlee.edu.tw","student_id":"11202330","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-04 23:01:11"},
    {"id":"49","email":"G1301106@gm.chihlee.edu.tw","student_id":"G1301106","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-04 23:11:09"},
    {"id":"51","email":"11102129@gm.chihlee.edu.tw","student_id":"11102129","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-04 23:27:57"},
    {"id":"52","email":"50902101@gm.chihlee.edu.tw","student_id":"50902101","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-04 23:31:34"},
    {"id":"57","email":"50707141@gm.chihlee.edu.tw","student_id":"50707141","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-05 07:32:37"},
    {"id":"58","email":"71302507@mail.chihlee.edu.tw","student_id":"71302507","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-05 08:34:35"},
    {"id":"60","email":"11313334@gm.chihlee.edu.tw","student_id":"11313334","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-05 09:06:14"},
    {"id":"62","email":"11008111@gm.chihlee.edu.tw","student_id":"11008111","token":"66d35b2fd94340eaec1dc3da5513407e6672b769","token_expiry":"1744084391285","verified":"0","created_at":"2025-04-05 11:53:08"},
    {"id":"64","email":"71313551@gm.chihlee.edu.tw","student_id":"71313551","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-05 12:00:00"},
    {"id":"67","email":"fuck@mail.chihlee.edu.tw","student_id":"fuck","token":"95b6ea9049573bd1ca5b2b21c995d735e8945424","token_expiry":"1744093172962","verified":"0","created_at":"2025-04-05 14:19:32"},
    {"id":"68","email":"51002106@gm.chihlee.edu.tw","student_id":"51002106","token":"fbdf3d3e3cb36874f0d457b64341b464d4683341","token_expiry":"1744100895988","verified":"0","created_at":"2025-04-05 16:23:33"},
    {"id":"72","email":"51002106@mail.chihlee.edu.tw","student_id":"51002106","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-05 16:29:12"},
    {"id":"84","email":"11110159@mail.chihlee.edu.tw","student_id":"11110159","token":"da8d2b99e3c54e646f45e05585ff472e6f5952d3","token_expiry":"1744122628138","verified":"0","created_at":"2025-04-05 22:30:28"},
    {"id":"85","email":"11110159@gm.chihlee.edu.tw","student_id":"11110159","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-05 22:31:30"},
    {"id":"104","email":"chlin.md11@nycu.edu.tw","student_id":"chlin.md11","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 00:53:46"},
    {"id":"106","email":"112111119@mail.aeust.edu.tw","student_id":"112111119","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 00:58:03"},
    {"id":"107","email":"s210127@email.nlhs.tyc.edu.tw","student_id":"s210127","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 00:58:40"},
    {"id":"110","email":"09360976@me.mcu.edu.tw","student_id":"09360976","token":"efe6f0cf8a664d6ac9350d65f9f4da7773575e30","token_expiry":"1744304464609","verified":"0","created_at":"2025-04-08 01:01:04"},
    {"id":"111","email":"09360972@me.mcu.edu.tw","student_id":"09360972","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 01:01:58"},
    {"id":"115","email":"B11323222@yuntech.edu.tw","student_id":"B11323222","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 01:04:37"},
    {"id":"118","email":"11135054@mail.hpsh.tp.edu.tw","student_id":"11135054","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 01:30:35"},
    {"id":"121","email":"A111280035@gm2.usc.edu.tw","student_id":"A111280035","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 01:34:58"},
    {"id":"122","email":"B1132025@niu.edu.tw","student_id":"B1132025","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 01:56:18"},
    {"id":"124","email":"B1132025@ems.niu.edu.tw","student_id":"B1132025","token":"7c32b9b0982d7644920adfcf280172f9a77f4cc4","token_expiry":"1744308246030","verified":"0","created_at":"2025-04-08 02:04:06"},
    {"id":"125","email":"u16111029@gs.ncku.edu.tw","student_id":"u16111029","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 02:05:59"},
    {"id":"126","email":"amu112105@gm.ntcu.edu.tw","student_id":"amu112105","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 02:06:06"},
    {"id":"128","email":"s1111302079@nutc.edu.tw","student_id":"s1111302079","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 02:07:29"},
    {"id":"130","email":"s1411302028@nutc.edu.tw","student_id":"s1411302028","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 02:31:36"},
    {"id":"131","email":"F1175801@cloud.dyu.edu.tw","student_id":"F1175801","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 03:01:49"},
    {"id":"132","email":"s0133691@go.edu.tw","student_id":"s0133691","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 03:37:30"},
    {"id":"135","email":"s51301416@student.szmc.edu.tw","student_id":"s51301416","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 03:44:11"},
    {"id":"136","email":"112536133@stu.ukn.edu.tw","student_id":"112536133","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 03:48:59"},
    {"id":"139","email":"u111003801@cmu.edu.tw","student_id":"u111003801","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 05:20:36"},
    {"id":"140","email":"10959129@gms.tcu.edu.tw","student_id":"10959129","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 05:46:48"},
    {"id":"143","email":"s1110244@std.hwhs.tc.edu.tw","student_id":"s1110244","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 05:58:54"},
    {"id":"144","email":"avery1234576@go.edu.tw","student_id":"avery1234576","token":"1d3c544feff07a12c1946109e138c8506b5ee8c0","token_expiry":"1744323824613","verified":"0","created_at":"2025-04-08 06:23:42"},
    {"id":"146","email":"11131308@gafe.cksh.tp.edu.tw","student_id":"11131308","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 06:57:16"},
    {"id":"148","email":"s11214096@cjc.edu.tw","student_id":"s11214096","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 07:02:53"},
    {"id":"149","email":"u110614@tcivs.tc.edu.tw","student_id":"u110614","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 07:08:17"},
    {"id":"154","email":"t112501042@mail.shu.edu.tw","student_id":"t112501042","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 07:14:43"},
    {"id":"155","email":"s0781@apps.ntpc.edu.tw","student_id":"s0781","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 07:17:13"},
    {"id":"156","email":"isu11008029A@isu.edu.tw","student_id":"isu11008029A","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 07:22:16"},
    {"id":"157","email":"weifang2019@mail.edu.tw","student_id":"weifang2019","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 07:22:19"},
    {"id":"159","email":"howard052699@apps.ntpc.edu.tw","student_id":"howard052699","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 07:24:32"},
    {"id":"160","email":"ba11213529@stu.ctas.tc.edu.tw","student_id":"ba11213529","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 07:27:11"},
    {"id":"161","email":"kfes103262@apps.ntpc.edu.tw","student_id":"kfes103262","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 07:27:38"},
    {"id":"163","email":"1120215@lmsh.tn.edu.tw","student_id":"1120215","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 07:30:18"},
    {"id":"164","email":"11130086@st1.ymsh.tp.edu.tw","student_id":"11130086","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 07:31:55"},
    {"id":"165","email":"ss310045@nehs.ptc.edu.tw","student_id":"ss310045","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 07:39:23"},
    {"id":"166","email":"std1212711@goo.tyai.tyc.edu.tw","student_id":"std1212711","token":"dbf2b154710296863ee384fe14212d3792f426e3","token_expiry":"1744328422057","verified":"0","created_at":"2025-04-08 07:40:22"},
    {"id":"167","email":"s210911131@student.nqu.edu.tw","student_id":"s210911131","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 07:41:56"},
    {"id":"168","email":"11210319@stmail.tcavs.tc.edu.tw","student_id":"11210319","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 07:41:57"},
    {"id":"169","email":"11111245@gm.chihlee.edu.tw","student_id":"11111245","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 07:42:31"},
    {"id":"171","email":"c113147345@nkust.edu.tw","student_id":"c113147345","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 07:44:18"},
    {"id":"174","email":"tu28291797@mail.edu.tw","student_id":"tu28291797","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 07:50:38"},
    {"id":"176","email":"pgpenguin72@gs.tp.edu.tw","student_id":"pgpenguin72","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 07:52:48"},
    {"id":"179","email":"s11101124@school.saihs.edu.tw","student_id":"s11101124","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 07:53:22"},
    {"id":"181","email":"cpshs311221@cpshs.hcc.edu.tw","student_id":"cpshs311221","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 07:57:54"},
    {"id":"184","email":"lisam.kh@go.edu.tw","student_id":"lisam.kh","token":"7dedeb653de0aa0767714a9106a27a36d6a56d50","token_expiry":"1744329588256","verified":"0","created_at":"2025-04-08 07:58:33"},
    {"id":"187","email":"11155225@st.nmjh.tp.edu.tw","student_id":"11155225","token":"72391d9d2ffe6d98b86972be722383077137484a","token_expiry":"1744329609830","verified":"0","created_at":"2025-04-08 08:00:09"},
    {"id":"188","email":"41114c076@gms.ndhu.edu.tw","student_id":"41114c076","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 08:07:31"},
    {"id":"190","email":"cliao7814@xxx.edu.tw","student_id":"cliao7814","token":"1bb1daa243e8f1c13b79690a4bbe1755e6a0b566","token_expiry":"1744330240121","verified":"0","created_at":"2025-04-08 08:10:38"},
    {"id":"192","email":"u112010017@cmu.edu.tw","student_id":"u112010017","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 08:12:51"},
    {"id":"193","email":"d1348935@o365.fcu.edu.tw","student_id":"d1348935","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 08:15:53"},
    {"id":"195","email":"s23110111@stu.edu.tw","student_id":"s23110111","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 08:20:52"},
    {"id":"196","email":"11208127@nkhs.to.edu.tw","student_id":"11208127","token":"6bb2683bcc5cd00a3bf96786594a3f1678a915a3","token_expiry":"1744331097565","verified":"0","created_at":"2025-04-08 08:24:56"},
    {"id":"198","email":"j1120304@gm.fdhs.tyc.edu.tw","student_id":"j1120304","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 08:35:21"},
    {"id":"200","email":"s50810045@student.szmc.edu.tw","student_id":"s50810045","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 08:58:48"},
    {"id":"201","email":"d13490043@gm.tut.edu.tw","student_id":"d13490043","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 09:04:16"},
    {"id":"202","email":"isu11155067a@go.isu.edu.tw","student_id":"isu11155067a","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 09:11:50"},
    {"id":"204","email":"cksh11331210@gafe.cksh.tp.edu.tw","student_id":"cksh11331210","token":"7536c9ac634d601b89827a883d3e8447650d5419","token_expiry":"1744334460449","verified":"0","created_at":"2025-04-08 09:21:00"},
    {"id":"205","email":"11331210@gafe.cksh.tp.edu.tw","student_id":"11331210","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 09:21:22"},
    {"id":"207","email":"3b313122@hm.student.ncut.edu.tw","student_id":"3b313122","token":"89e9e16bac1ee4f5a271995719cd3ebf1171c2b7","token_expiry":"1744335039838","verified":"0","created_at":"2025-04-08 09:30:39"},
    {"id":"208","email":"3b313122@gm.student.ncut.edu.tw","student_id":"3b313122","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 09:30:57"},
    {"id":"209","email":"c109072@schoil.saihs.edu.tw","student_id":"c109072","token":"7d21fbb79fa90727a71af69ae8a98a89ce3560c7","token_expiry":"1744335987516","verified":"0","created_at":"2025-04-08 09:46:27"},
    {"id":"210","email":"c109072@school.saihs.edu.tw","student_id":"c109072","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 09:46:32"},
    {"id":"211","email":"s1111032015@nutc.edu.tw","student_id":"s1111032015","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 09:49:36"},
    {"id":"212","email":"s11317032@gm.cyut.edu.tw","student_id":"s11317032","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 09:54:37"},
    {"id":"214","email":"zhengmingxiang@mail.edu.tw","student_id":"zhengmingxiang","token":"2ceffec74e31bf210ae2043e9a82c715fec89f27","token_expiry":"1744336720885","verified":"0","created_at":"2025-04-08 09:58:40"},
    {"id":"215","email":"310195@mail.pcsh.ntpc.edu.tw","student_id":"310195","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 10:00:08"},
    {"id":"216","email":"310195@pcsh.ntpc.edu.tw","student_id":"310195","token":"a72d109e1a0ffa10eae06d43c3d3a8ce68779344","token_expiry":"1744336965738","verified":"0","created_at":"2025-04-08 10:02:45"},
    {"id":"217","email":"11230267@dcsh.tp.edu.tw","student_id":"11230267","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 10:07:12"},
    {"id":"218","email":"111192@stu.nknush.kh.edu.tw","student_id":"111192","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 10:18:20"},
    {"id":"219","email":"s111075@ms.cshs.tc.edu.tw","student_id":"s111075","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 10:19:06"},
    {"id":"221","email":"s1315232@taivs.tp.edu.tw","student_id":"s1315232","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 11:07:43"},
    {"id":"222","email":"a@pccu.edu.tw","student_id":"a","token":"bf38cef6934fdc715c3123b4e9876a29e8344460","token_expiry":"1744341214120","verified":"0","created_at":"2025-04-08 11:13:34"},
    {"id":"223","email":"4b1l0070@stust.edu.tw","student_id":"4b1l0070","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 11:40:34"},
    {"id":"224","email":"s1123110@mail.yzu.edu.tw","student_id":"s1123110","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 11:40:57"},
    {"id":"225","email":"s111314013@stu.ntue.edu.tw","student_id":"s111314013","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 11:45:53"},
    {"id":"226","email":"41139256@gcloud.csu.edu.tw","student_id":"41139256","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 11:46:10"},
    {"id":"227","email":"13260186@me.mcu.edu.tw","student_id":"13260186","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 12:29:44"},
    {"id":"228","email":"41242109S@ntnu.edu.tw","student_id":"41242109S","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 12:35:48"},
    {"id":"229","email":"sung0907@apps.ntpc.edu.tw","student_id":"sung0907","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 12:41:32"},
    {"id":"230","email":"511101150@std.mlc.edu.tw","student_id":"511101150","token":"50dd728f9e4684b6f502cfe24d4b852ce00ff5fd","token_expiry":"1744346794631","verified":"0","created_at":"2025-04-08 12:46:34"},
    {"id":"231","email":"n26101648@gs.ncku.edu.tw","student_id":"n26101648","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 12:49:31"},
    {"id":"232","email":"811015@mail.jlsh.edu.tw","student_id":"811015","token":"093495cdd6e8d8d338b4c8f21873c359678bb7a6","token_expiry":"1744347470785","verified":"0","created_at":"2025-04-08 12:57:50"},
    {"id":"233","email":"11121020@nhu.edu.tw","student_id":"11121020","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 12:59:20"},
    {"id":"234","email":"g109102518@g.ncu.edu.tw","student_id":"g109102518","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 12:59:59"},
    {"id":"235","email":"s11330043@zlsh.tp.edu.tw","student_id":"s11330043","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 13:04:27"},
    {"id":"236","email":"u1210008@o365.nuu.edu.tw","student_id":"u1210008","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 13:11:48"},
    {"id":"237","email":"1120f027@mail1.yudah.tp.edu.tw","student_id":"1120f027","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 13:15:38"},
    {"id":"240","email":"13750041@me.mcu.edu.tw","student_id":"13750041","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 13:21:52"},
    {"id":"242","email":"b0911030@gm.cnu.edu.tw","student_id":"b0911030","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 13:23:05"},
    {"id":"243","email":"111302554@cc.ncu.edu.tw","student_id":"111302554","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 13:23:48"},
    {"id":"246","email":"a111400207@mail.shu.edu.tw","student_id":"a111400207","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 13:25:51"},
    {"id":"249","email":"s511201402@ntin.edu.tw","student_id":"s511201402","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 13:30:40"},
    {"id":"250","email":"111601069@g.nccu.edu.tw","student_id":"111601069","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 13:32:17"},
    {"id":"251","email":"b3201177@ulive.pccu.edu.tw","student_id":"b3201177","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 13:36:19"},
    {"id":"254","email":"L76134046@gs.ncku.edu.tw","student_id":"L76134046","token":"a3b744bb5615de63d8fd688a47207379904dd040","token_expiry":"1744350075240","verified":"0","created_at":"2025-04-08 13:41:15"},
    {"id":"255","email":"11130201@ms2.hssh.tp.edu.tw","student_id":"11130201","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 13:41:34"},
    {"id":"256","email":"L76134047@gs.ncku.edu.tw","student_id":"L76134047","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 13:42:14"},
    {"id":"257","email":"st1112300040@wzu.edu.tw","student_id":"st1112300040","token":"bcc044364cec47b932a5d9663104225d27979fee","token_expiry":"1744350414637","verified":"0","created_at":"2025-04-08 13:46:53"},
    {"id":"259","email":"b812112033@tmu.edu.tw","student_id":"b812112033","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 13:47:22"},
    {"id":"260","email":"1112300040@st112.wzu.edu.tw","student_id":"1112300040","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 13:48:23"},
    {"id":"261","email":"yukai.ee12@nycu.edu.tw","student_id":"yukai.ee12","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 13:51:23"},
    {"id":"262","email":"11313120@gm.nttu.edu.tw","student_id":"11313120","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 13:53:27"},
    {"id":"266","email":"41211147@gcloud.csu.edu.tw","student_id":"41211147","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 14:02:45"},
    {"id":"267","email":"s111254@ms.cshs.tc.edu.tw","student_id":"s111254","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 14:06:22"},
    {"id":"270","email":"b08209010@ntu.edu.tw","student_id":"b08209010","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 14:10:48"},
    {"id":"271","email":"s0402107@mail.edu.tw","student_id":"s0402107","token":"b84b9dbf6cffee28dd53a4898f1be7bc6e00275e","token_expiry":"1744352006824","verified":"0","created_at":"2025-04-08 14:13:26"},
    {"id":"272","email":"s0402107@go.edu.tw","student_id":"s0402107","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 14:13:39"},
    {"id":"274","email":"s24310616@fssh.khc.edu.tw","student_id":"s24310616","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 14:15:13"},
    {"id":"276","email":"113105109@gms.tcu.edu.tw","student_id":"113105109","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 14:19:20"},
    {"id":"277","email":"31v485@ms.mingdao.edu.tw","student_id":"31v485","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 14:27:06"},
    {"id":"279","email":"kai329@nptu.edu.tw","student_id":"kai329","token":"0cfd9b957ba5b2eb62cdb4790c7e7ec1e92d0ee6","token_expiry":"1744352932414","verified":"0","created_at":"2025-04-08 14:27:27"},
    {"id":"281","email":"411430811@o365.tku.edu.tw","student_id":"411430811","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 14:36:17"},
    {"id":"285","email":"s110371@stmail.hhsh.chc.edu.tw","student_id":"s110371","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 14:41:08"},
    {"id":"286","email":"chiachengkuo1026@go.edu.tw","student_id":"chiachengkuo1026","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 14:43:31"},
    {"id":"287","email":"K11348020@mail.npust.edu.tw","student_id":"K11348020","token":"1590a8c77868ef9fd070c293cd34e811994d5dc4","token_expiry":"1744353849046","verified":"0","created_at":"2025-04-08 14:44:09"},
    {"id":"288","email":"K11348020@st.npust.edu.tw","student_id":"K11348020","token":"708db5cff365ca7f24262cbae7a425c2223cbd5e","token_expiry":"1744354016356","verified":"0","created_at":"2025-04-08 14:46:02"},
    {"id":"295","email":"B11337017@chu.edu.tw","student_id":"B11337017","token":"2f7fae778f3512dca9acedf2de2f1bbeb793dfd4","token_expiry":"1744353978595","verified":"0","created_at":"2025-04-08 14:46:18"},
    {"id":"299","email":"s11114054@o365.cyut.edu.tw","student_id":"s11114054","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 14:47:17"},
    {"id":"300","email":"ASC110110@gm.ntcu.edu.tw","student_id":"ASC110110","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 14:49:27"},
    {"id":"301","email":"111105206@mail.aeust.edu.tw","student_id":"111105206","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 14:51:24"},
    {"id":"302","email":"s11114054@cyut.edu.tw","student_id":"s11114054","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 14:52:27"},
    {"id":"303","email":"s1100946@mail.yzu.edu.tw","student_id":"s1100946","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 15:07:33"},
    {"id":"304","email":"11008315@gm.chihlee.edu.tw","student_id":"11008315","token":"c8496bb934d6684397b040fff75fecc1788eacd9","token_expiry":"1744355720022","verified":"0","created_at":"2025-04-08 15:15:18"},
    {"id":"308","email":"11355020@tpsh.tp.edu.tw","student_id":"11355020","token":"17ef3e72774ba8ec9b676601ee636c074d636046","token_expiry":"1744356277334","verified":"0","created_at":"2025-04-08 15:24:37"},
    {"id":"309","email":"11355010@tpsh.tp.edu.tw","student_id":"11355010","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 15:24:51"},
    {"id":"313","email":"s23108113@stu.edu.tw","student_id":"s23108113","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 15:25:56"},
    {"id":"315","email":"113121908@webmail.nou.edu.tw","student_id":"113121908","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 15:27:14"},
    {"id":"316","email":"411222040@gms.ndhu.edu.tw","student_id":"411222040","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 15:28:25"},
    {"id":"317","email":"112703023@nccu.edu.tw","student_id":"112703023","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 15:34:27"},
    {"id":"319","email":"C113154127@nkust.edu.tw","student_id":"C113154127","token":"0e7913edb5f6ae28e250ba4b341ea193de1f301a","token_expiry":"1744357268991","verified":"0","created_at":"2025-04-08 15:41:08"},
    {"id":"320","email":"d12407020@ems.npu.edu.tw","student_id":"d12407020","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 16:09:23"},
    {"id":"322","email":"113068@jajh.hcc.edu.tw","student_id":"113068","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 16:10:28"},
    {"id":"323","email":"hsbs@cyut.edu.tw","student_id":"hsbs","token":"7a60ade16b3ecd187b509e6d0c0be49be21aedc1","token_expiry":"1744360311444","verified":"0","created_at":"2025-04-08 16:31:51"},
    {"id":"325","email":"s1163047@gm.ncue.edu.tw","student_id":"s1163047","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 16:33:16"},
    {"id":"328","email":"11101170@gm.nttu.edu.tw","student_id":"11101170","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 16:34:53"},
    {"id":"330","email":"1131440021@gm.cute.edu.tw","student_id":"1131440021","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 16:45:42"},
    {"id":"331","email":"413402435@m365.fju.edu.tw","student_id":"413402435","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 16:48:55"},
    {"id":"332","email":"s112019@yrhs.tn.edu.tw","student_id":"s112019","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 17:03:43"},
    {"id":"334","email":"dhjh121255051@dhjh.tp.edu.tw","student_id":"dhjh121255051","token":"84dae70a2ae1391a08a34572c95c13e1dc58b4fc","token_expiry":"1744362829456","verified":"0","created_at":"2025-04-08 17:13:49"},
    {"id":"335","email":"dhjh11255051@dhjh.tp.edu.tw","student_id":"dhjh11255051","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 17:14:21"},
    {"id":"337","email":"hy106019@chc.edu.tw","student_id":"hy106019","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 17:17:15"},
    {"id":"338","email":"c113196138@nkust.edu.tw","student_id":"c113196138","token":"c98088383ea3fc21667e49d2aa70f807dc3f8e6f","token_expiry":"1744363296728","verified":"0","created_at":"2025-04-08 17:21:36"},
    {"id":"339","email":"s122266@yfms.tyc.edu.tw","student_id":"s122266","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 17:23:51"},
    {"id":"340","email":"1110063@lgjh.ptc.edu.tw","student_id":"1110063","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 17:29:01"},
    {"id":"341","email":"11235230@tp.edu.tw","student_id":"11235230","token":"9c63dfee96a7072d932fac9ded32c383f187a1d5","token_expiry":"1744364336121","verified":"0","created_at":"2025-04-08 17:38:56"},
    {"id":"342","email":"11235230@gs.tp.edu.tw","student_id":"11235230","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 17:44:23"},
    {"id":"344","email":"B3203684@ulive.pccu.edu.tw","student_id":"B3203684","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 17:50:55"},
    {"id":"345","email":"1111410035@mail.hwu.edu.tw","student_id":"1111410035","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 17:53:15"},
    {"id":"346","email":"s1112402@mail.nljh.tyc.edu.tw","student_id":"s1112402","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 18:14:53"},
    {"id":"347","email":"s311249005@gm.ntpu.edu.tw","student_id":"s311249005","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 18:24:55"},
    {"id":"349","email":"11410260@me.mcu.edu.tw","student_id":"11410260","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 18:42:08"},
    {"id":"352","email":"41043113S@gapps.ntnu.edu.tw","student_id":"41043113S","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 18:52:35"},
    {"id":"354","email":"111125@gsuite.essh.kl.edu.tw","student_id":"111125","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 18:56:46"},
    {"id":"355","email":"317042@wufai.tc.edu.tw","student_id":"317042","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 18:57:36"},
    {"id":"359","email":"s211311@nocsh.ntpc.edu.tw","student_id":"s211311","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 19:00:41"},
    {"id":"360","email":"113510547@ctcn.edu.tw","student_id":"113510547","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 19:01:54"},
    {"id":"362","email":"d1158330@fcu.edu.tw","student_id":"d1158330","token":"34f708ada7f1223415adb592ca347de01c38af3c","token_expiry":"1744369627908","verified":"0","created_at":"2025-04-08 19:07:07"},
    {"id":"363","email":"1110126@hsjh.ptc.edu.tw","student_id":"1110126","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 19:16:07"},
    {"id":"364","email":"pocheng@smail.ilc.edu.tw","student_id":"pocheng","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 19:23:42"},
    {"id":"365","email":"fzr@g2.usc.edu.tw","student_id":"fzr","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 19:26:33"},
    {"id":"366","email":"db317026@gm.student.ncut.edu.tw","student_id":"db317026","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 19:34:06"},
    {"id":"368","email":"110403566@cc.ncu.edu.tw","student_id":"110403566","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 19:41:59"},
    {"id":"369","email":"s211008@ntsh.ntct.edu.tw","student_id":"s211008","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 19:46:54"},
    {"id":"371","email":"st-super-25@tp.edu.tw","student_id":"st-super-25","token":"b56814df3b66bc405f3322893bf1db3a219cf270","token_expiry":"1744372022533","verified":"0","created_at":"2025-04-08 19:47:02"},
    {"id":"372","email":"st-super-25@gs.tp.edu.tw","student_id":"st-super-25","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 19:48:07"},
    {"id":"375","email":"41318006@mail2u.tnu.edu.tw","student_id":"41318006","token":"504b9ecd13dd12a99d68e078d8dcf7607c908601","token_expiry":"1744373468567","verified":"0","created_at":"2025-04-08 20:11:08"},
    {"id":"376","email":"cce113001@nptu.edu.tw","student_id":"cce113001","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 20:21:53"},
    {"id":"383","email":"sam970208@apps.ntpc.edu.tw","student_id":"sam970208","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 20:27:00"},
    {"id":"384","email":"s11316021@fsvs.khc.edu.tw","student_id":"s11316021","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 20:52:03"},
    {"id":"387","email":"cdj111007@nptu.edu.tw","student_id":"cdj111007","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 20:54:57"},
    {"id":"388","email":"120344@student.kshs.edu.tw","student_id":"120344","token":"d3c101d9b5593d902eadb595e70075b985b26df6","token_expiry":"1744376134315","verified":"0","created_at":"2025-04-08 20:55:34"},
    {"id":"393","email":"1110110@school.dam.kh.edu.tw","student_id":"1110110","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 20:59:26"},
    {"id":"394","email":"s311249014@gm.ntpu.edu.tw","student_id":"s311249014","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 21:06:57"},
    {"id":"395","email":"11131055@st.fhjh.tp.edu.tw","student_id":"11131055","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 21:24:31"},
    {"id":"396","email":"bossji038@alum.ccu.edu.tw","student_id":"bossji038","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 21:28:30"},
    {"id":"397","email":"3b313148@gm.student.ncut.edu.tw","student_id":"3b313148","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 21:41:30"},
    {"id":"398","email":"11251023@st.fhjh.tp.edu.tw","student_id":"11251023","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 21:45:45"},
    {"id":"401","email":"a9606165678@apps.ntpc.edu.tw","student_id":"a9606165678","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 21:57:13"},
    {"id":"405","email":"1111440015@gm.cute.edu.tw","student_id":"1111440015","token":"6fb987f6419c739c732aa079a28eef0eca2428fa","token_expiry":"1744380338783","verified":"0","created_at":"2025-04-08 22:01:34"},
    {"id":"408","email":"826114@st.tc.edu.tw","student_id":"826114","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 22:08:15"},
    {"id":"411","email":"s112y0531@jdjh.ntpc.edu.tw","student_id":"s112y0531","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 22:30:18"},
    {"id":"414","email":"s411372041@gm.ntpu.edu.tw","student_id":"s411372041","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 22:33:29"},
    {"id":"418","email":"a9683065@ulive.pccu.edu.tw","student_id":"a9683065","token":"c780f0ae7943b8e7598200bc47a6936968680b0d","token_expiry":"1744382114835","verified":"0","created_at":"2025-04-08 22:35:14"},
    {"id":"420","email":"113015@shsh.kl.edu.tw","student_id":"113015","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 22:44:37"},
    {"id":"422","email":"s0609300@go.edu.tw","student_id":"s0609300","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 23:04:46"},
    {"id":"423","email":"111021@bmjh.ntct.edu.tw","student_id":"111021","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 23:04:52"},
    {"id":"424","email":"s3b011233@ncut.edu.tw","student_id":"s3b011233","token":"7f7c8b08bcea96fa7401cd91d9b44ea366d10a1e","token_expiry":"1744386802041","verified":"0","created_at":"2025-04-08 23:53:20"},
    {"id":"426","email":"3b011233@gm.student.ncut.edu.tw","student_id":"3b011233","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-08 23:54:20"},
    {"id":"427","email":"411540053@student.tajen.edu.tw","student_id":"411540053","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-09 00:20:50"},
    {"id":"428","email":"11031005@nhu.edu.tw","student_id":"11031005","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-09 00:29:11"},
    {"id":"430","email":"s311114@whsh.tc.edu.tw","student_id":"s311114","token":"ef42232fc3de8cf98290efef4903e47b886b4287","token_expiry":"1744394524331","verified":"0","created_at":"2025-04-09 02:02:01"},
    {"id":"432","email":"b34131402@gs.ncku.edu.tw","student_id":"b34131402","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-09 02:30:25"},
    {"id":"433","email":"goodgood@ntu.edu.tw","student_id":"goodgood","token":"b7c8a6929bbc9cf3fb2b13e42597ae3784ed643a","token_expiry":"1744413772003","verified":"0","created_at":"2025-04-09 07:22:50"},
    {"id":"435","email":"joshncu@g.ncu.edu.tw","student_id":"joshncu","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-09 10:32:52"},
    {"id":"436","email":"111212@student.kjsh.ntpc.edu.tw","student_id":"111212","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-09 11:01:48"},
    {"id":"437","email":"l102233@apps.ntpc.edu.tw","student_id":"l102233","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-09 11:08:44"},
    {"id":"440","email":"11323201@gm.chihlee.edu.tw","student_id":"11323201","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-09 17:32:17"},
    {"id":"441","email":"m11313023@yuntech.edu.tw","student_id":"m11313023","token":None,"token_expiry":None,"verified":"1","created_at":"2025-04-09 19:55:43"}
]

# 已知之對照表(只截取對話中提供的部分)
knownDomains = {
     'gm.chihlee.edu.tw': '致理科技大學',
    'mail.chihlee.edu.tw': '致理科技大學',
    'chihlee.edu.tw': '致理科技大學',
    'ntu.edu.tw': '國立臺灣大學',
    'nthu.edu.tw': '國立清華大學',
    'ncku.edu.tw': '國立成功大學',
    'nctu.edu.tw': '國立交通大學',
    'nsysu.edu.tw': '國立中山大學',
    'nchu.edu.tw': '國立中興大學',
    'nccu.edu.tw': '國立政治大學',
    'ntnu.edu.tw': '國立臺灣師範大學',
    'ncu.edu.tw': '國立中央大學',
    'ccu.edu.tw': '國立中正大學',
    'ntust.edu.tw': '國立臺灣科技大學',
    'ntut.edu.tw': '國立臺北科技大學',
    'nkust.edu.tw': '國立高雄科技大學',
    'ntua.edu.tw': '國立臺灣藝術大學',
    'tnnua.edu.tw': '國立臺南藝術大學',
    'nycu.edu.tw': '國立陽明交通大學',
    'ntou.edu.tw': '國立臺灣海洋大學',
    'niu.edu.tw': '國立宜蘭大學',
    'ntcu.edu.tw': '國立臺中教育大學',
    'ncue.edu.tw': '國立彰化師範大學',
    'yuntech.edu.tw': '國立雲林科技大學',
    'ncyu.edu.tw': '國立嘉義大學',
    'npust.edu.tw': '國立屏東科技大學',
    'nttu.edu.tw': '國立臺東大學',
    'nknu.edu.tw': '國立高雄師範大學',
    'ndhu.edu.tw': '國立東華大學',
    'ncnu.edu.tw': '國立暨南國際大學',
    'ntpu.edu.tw': '國立臺北大學',
    'ntus.edu.tw': '國立臺灣體育運動大學',
    'ntunhs.edu.tw': '國立臺北護理健康大學',
    'nfu.edu.tw': '國立虎尾科技大學',
    'nkuht.edu.tw': '國立高雄餐旅大學',
    'tcpa.edu.tw': '國立臺灣戲曲學院',
    'nou.edu.tw': '國立空中大學',
    'ncut.edu.tw': '國立勤益科技大學',
    'ntub.edu.tw': '國立臺北商業大學',
    'nutc.edu.tw': '國立臺中科技大學',
    'nkfust.edu.tw': '國立高雄第一科技大學',
    'kuas.edu.tw': '國立高雄應用科技大學',
    'ntcpe.edu.tw': '國立臺灣體育學院',
    'ntue.edu.tw': '國立臺北教育大學',
    'nptu.edu.tw': '國立屏東大學',
    'ntc.edu.tw': '國立臺東專科學校',
    'ntin.edu.tw': '國立臺南護理專科學校',
    "scu.edu.tw": "東吳大學",
    "fju.edu.tw": "輔仁大學",
    "thu.edu.tw": "東海大學",
    "tku.edu.tw": "淡江大學",
    "fcu.edu.tw": "逢甲大學",
    "cycu.edu.tw": "中原大學",
    "cmu.edu.tw": "中國醫藥大學",
    "tmu.edu.tw": "臺北醫學大學",
    "mcu.edu.tw": "銘傳大學",
    "shu.edu.tw": "世新大學",
    "usc.edu.tw": "實踐大學",
    "ttu.edu.tw": "大同大學",
    "pccu.edu.tw": "中國文化大學",
    "pu.edu.tw": "靜宜大學",
    "cgu.edu.tw": "長庚大學",
    "yzu.edu.tw": "元智大學",
    "kmu.edu.tw": "高雄醫學大學",
    "isu.edu.tw": "義守大學",
    "cju.edu.tw": "長榮大學",
    "csmu.edu.tw": "中山醫學大學",
    "huafan.edu.tw": "華梵大學",
    "chu.edu.tw": "中華大學",
    "dyu.edu.tw": "大葉大學",
    "au.edu.tw": "真理大學",
    "tcu.edu.tw": "慈濟大學",
    "nhu.edu.tw": "南華大學",
    "hcu.edu.tw": "玄奘大學",
    "fgu.edu.tw": "佛光大學",
    "ukn.edu.tw": "康寧大學",
    "asia.edu.tw": "亞洲大學",
    "knu.edu.tw": "開南大學",
    "mmc.edu.tw": "馬偕醫學院",
    "dila.edu.tw": "法鼓文理學院",
    "ctbc.edu.tw": "中信金融管理學院",
    "mcut.edu.tw": "明志科技大學",
    "csu.edu.tw": "正修科技大學",
    "hwu.edu.tw": "醒吾科技大學",
    "fy.edu.tw": "輔英科技大學",
    "tpcu.edu.tw": "臺北城市科技大學",
    "mitust.edu.tw": "敏實科技大學",
    "pcsh.ntpc.edu.tw": "新北市立板橋高中",
    "cyut.edu.tw": "朝陽科技大學",
    "rhs.tn.edu.tw": "臺南市立永仁高級中學",
    "tsh.ntct.edu.tw.edu.tw": "國立南投高級中學",
    "kjsh.ntpc.edu.tw": "新北市光仁高級中學"
}

# 設置 Pandas 顯示選項，讓它不會省略 Rows：
pd.set_option('display.max_rows', None)

# 同理，如果你想不省略 Column：
pd.set_option('display.max_columns', None)


# ======= (3) unify_domain 函式 =======
def unify_domain(domain):
    """
    如果是 xxx.edu.tw 形式，就取最後 3 段；若在 knownDomains 中，則回傳該基底網域。
    若找不到，則嘗試從左至右(去除子網域)匹配 knownDomains；若都失敗則回傳原 domain 或標示 "未知"。
    """
    segments = domain.split('.')
    
    # 若符合 *.edu.tw，先取最後三段
    if len(segments) >= 3 and segments[-2] == 'edu' and segments[-1] == 'tw':
        base_candidate = ".".join(segments[-3:])
    else:
        # 若不符合 *.edu.tw，先直接使用整個 domain
        base_candidate = domain

    # 如果 base_candidate 在 knownDomains，直接回傳
    if base_candidate in knownDomains:
        return base_candidate
    
    # 若不在 knownDomains，嘗試自左至右去除子網域
    for i in range(len(segments)):
        candidate = ".".join(segments[i:])
        if candidate in knownDomains:
            return candidate

    # 全找不到 => 就回傳 base_candidate (可以理解成「未知」)
    return base_candidate


# ======= (4) get_school_name 函式 =======
def get_school_name(d):
    return knownDomains.get(d, "未知")


# ======= (5) 主程式邏輯 =======
if __name__ == "__main__":
    # 將 raw_data 做成 DataFrame
    df = pd.DataFrame(raw_data)

    # 過濾：token 為 None (即尚無 token 資料者)
    df_filtered = df[df['token'].isnull()].copy()

    # 取出 domain
    df_filtered['domain'] = df_filtered['email'].apply(lambda x: x.split('@', 1)[1].lower())

    # 統一化 domain
    df_filtered['unified_domain'] = df_filtered['domain'].apply(unify_domain)

    # 分組計算
    domain_counts = df_filtered.groupby('unified_domain').size().reset_index(name='count')

    # 加上「學校名字」欄位
    domain_counts['學校名字'] = domain_counts['unified_domain'].apply(get_school_name)

    # 整理欄位
    domain_counts = domain_counts.rename(columns={
        'unified_domain': '學校域名',
        'count': '驗證次數'
    })
    domain_counts = domain_counts[['學校名字', '學校域名', '驗證次數']]

    # 排序：驗證次數大到小
    domain_counts = domain_counts.sort_values('驗證次數', ascending=False).reset_index(drop=True)

    # 印出結果
    print(domain_counts)