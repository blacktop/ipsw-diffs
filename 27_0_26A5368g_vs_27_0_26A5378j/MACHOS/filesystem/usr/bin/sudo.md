## sudo

> `/usr/bin/sudo`

```diff

-  __TEXT.__text: 0x7f688
+  __TEXT.__text: 0x7f4b8
   __TEXT.__auth_stubs: 0x1070
   __TEXT.__cstring: 0x17573
   __TEXT.__const: 0xcd10
Sections:
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
~ __DATA.__common : content changed
Functions:
~ sub_100002314 : 388 -> 364
~ sub_10000b29c -> sub_10000b284 : 1068 -> 1048
~ sub_100010290 -> sub_100010264 : 548 -> 556
~ sub_1000122b0 -> sub_10001228c : 3548 -> 3540
~ sub_10001415c -> sub_100014130 : 288 -> 272
~ sub_10001427c -> sub_100014240 : 408 -> 392
~ sub_100014414 -> sub_1000143c8 : 664 -> 648
~ sub_1000146c0 -> sub_100014664 : 304 -> 312
~ sub_10001948c -> sub_100019438 : 576 -> 564
~ sub_100022dc8 -> sub_100022d68 : 932 -> 924
~ sub_10002368c -> sub_100023624 : 860 -> 868
~ sub_100024088 -> sub_100024028 : 256 -> 272
~ sub_1000242a0 -> sub_100024250 : 256 -> 272
~ sub_100025ca4 -> sub_100025c64 : 2840 -> 2832
~ sub_10002871c -> sub_1000286d4 : 684 -> 672
~ sub_100028c10 -> sub_100028bbc : 1820 -> 1824
~ sub_100029698 -> sub_100029648 : 652 -> 620
~ sub_100029924 -> sub_1000298b4 : 916 -> 892
~ sub_100029cb8 -> sub_100029c30 : 496 -> 520
~ sub_10002aa80 -> sub_10002aa10 : 316 -> 320
~ sub_10002bc20 -> sub_10002bbb4 : 188 -> 216
~ sub_10003362c -> sub_1000335dc : 708 -> 648
~ sub_1000338f0 -> sub_100033864 : 320 -> 308
~ sub_100033a30 -> sub_100033998 : 336 -> 320
~ sub_100033b80 -> sub_100033ad8 : 1468 -> 1420
~ sub_1000343b8 -> sub_1000342e0 : 332 -> 316
~ sub_100034504 -> sub_10003441c : 260 -> 252
~ sub_100034608 -> sub_100034518 : 292 -> 276
~ sub_100035050 -> sub_100034f50 : 560 -> 552
~ sub_1000352d4 -> sub_1000351cc : 496 -> 484
~ sub_1000354f8 -> sub_1000353e4 : 476 -> 464
~ sub_100035c18 -> sub_100035af8 : 324 -> 316
~ sub_100036230 -> sub_100036108 : 2088 -> 2076
~ sub_100037420 -> sub_1000372ec : 784 -> 740
~ sub_100044b5c -> sub_1000449fc : 156 -> 132
~ sub_100044bf8 -> sub_100044a80 : 156 -> 132
~ sub_10004a23c -> sub_10004a0ac : 5200 -> 5224
~ sub_100051464 -> sub_1000512ec : 332 -> 316
~ sub_100059388 -> sub_100059200 : 1108 -> 1112
~ sub_10005c3ac -> sub_10005c228 : 364 -> 348
~ sub_10005caf4 -> sub_10005c960 : 304 -> 292
~ sub_10005e570 -> sub_10005e3d0 : 5940 -> 5928
~ sub_1000641c0 -> sub_100064014 : 4856 -> 4888
~ sub_10006c6a4 -> sub_10006c518 : 15272 -> 15256
~ sub_100071290 -> sub_1000710f4 : 4512 -> 4500
~ sub_10007243c -> sub_100072294 : 340 -> 328
~ sub_100072f04 -> sub_100072d50 : 264 -> 256
~ sub_1000757ec -> sub_100075630 : 1696 -> 1672
~ sub_100077104 -> sub_100076f30 : 772 -> 780
~ sub_100079400 -> sub_100079234 : 476 -> 468
~ sub_10007b04c -> sub_10007ae78 : 576 -> 572
~ sub_10007b484 -> sub_10007b2ac : 740 -> 744
~ sub_10007b768 -> sub_10007b594 : 3740 -> 3744
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/eventlog/eventlog.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/eventlog/eventlog_conf.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/eventlog/eventlog_free.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/eventlog/logwrap.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/eventlog/parse_json.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/iolog/host_port.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/iolog/iolog_close.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/iolog/iolog_conf.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/iolog/iolog_filter.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/iolog/iolog_json.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/iolog/iolog_legacy.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/iolog/iolog_loginfo.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/iolog/iolog_mkdirs.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/iolog/iolog_mkdtemp.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/iolog/iolog_mkpath.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/iolog/iolog_nextid.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/iolog/iolog_open.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/iolog/iolog_openat.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/iolog/iolog_path.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/iolog/iolog_swapids.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/iolog/iolog_util.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/iolog/iolog_write.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/digest.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/event.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/event_select.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/getgrouplist.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/gettime.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/gidlist.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/hexchar.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/json.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/key_val.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/lbuf.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/locking.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/logfac.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/logpri.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/mkdir_parents.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/parseln.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/rcstr.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/regex.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/secure_path.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/setgroups.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/strsplit.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/strtobool.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/strtoid.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/strtomode.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/sudo_conf.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/term.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/ttyname_dev.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/ttysize.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/alias.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/audit.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/auth/pam.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/auth/sudo_auth.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/b64_decode.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/boottime.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/canon_path.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/check.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/check_util.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/defaults.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/digestname.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/display.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/editor.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/env.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/env_pattern.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/exptilde.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/file.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/filedigest.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/find_path.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/fmtsudoers.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/gentime.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/goodpath.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/group_plugin.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/interfaces.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/iolog.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/iolog_path_escapes.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/locale.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/log_client.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/logging.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/lookup.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/match.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/match_addr.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/match_command.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/match_digest.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/parser_warnx.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/policy.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/prompt.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/pwutil.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/pwutil_impl.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/redblack.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/resolve_cmnd.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/serialize_list.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/set_perms.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/sethost.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/starttime.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/strlcpy_unesc.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/strlist.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/strvec_join.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/sudo_nss.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/sudoers.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/sudoers_cb.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/sudoers_ctx_free.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/sudoers_debug.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/timeout.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/timestamp.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/toke_util.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/src/copy_file.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/src/edit_open.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/src/exec.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/src/exec_common.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/src/exec_intercept.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/src/exec_iolog.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/src/exec_monitor.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/src/exec_nopty.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/src/exec_preload.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/src/exec_ptrace.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/src/exec_pty.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/src/get_pty.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/src/hooks.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/src/limits.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/src/load_plugins.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/src/net_ifs.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/src/parse_args.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/src/preserve_fds.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/src/signal.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/src/sudo.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/src/sudo_edit.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/src/suspend_parent.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/src/tgetpass.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/src/ttyname.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/src/utmp.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/eventlog/eventlog.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/eventlog/eventlog_conf.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/eventlog/eventlog_free.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/eventlog/logwrap.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/eventlog/parse_json.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/iolog/host_port.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/iolog/iolog_close.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/iolog/iolog_conf.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/iolog/iolog_filter.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/iolog/iolog_json.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/iolog/iolog_legacy.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/iolog/iolog_loginfo.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/iolog/iolog_mkdirs.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/iolog/iolog_mkdtemp.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/iolog/iolog_mkpath.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/iolog/iolog_nextid.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/iolog/iolog_open.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/iolog/iolog_openat.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/iolog/iolog_path.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/iolog/iolog_swapids.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/iolog/iolog_util.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/iolog/iolog_write.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/digest.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/event.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/event_select.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/getgrouplist.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/gettime.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/gidlist.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/hexchar.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/json.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/key_val.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/lbuf.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/locking.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/logfac.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/logpri.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/mkdir_parents.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/parseln.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/rcstr.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/regex.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/secure_path.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/setgroups.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/strsplit.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/strtobool.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/strtoid.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/strtomode.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/sudo_conf.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/term.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/ttyname_dev.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/ttysize.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/alias.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/audit.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/auth/pam.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/auth/sudo_auth.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/b64_decode.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/boottime.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/canon_path.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/check.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/check_util.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/defaults.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/digestname.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/display.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/editor.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/env.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/env_pattern.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/exptilde.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/file.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/filedigest.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/find_path.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/fmtsudoers.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/gentime.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/goodpath.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/group_plugin.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/interfaces.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/iolog.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/iolog_path_escapes.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/locale.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/log_client.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/logging.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/lookup.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/match.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/match_addr.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/match_command.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/match_digest.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/parser_warnx.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/policy.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/prompt.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/pwutil.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/pwutil_impl.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/redblack.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/resolve_cmnd.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/serialize_list.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/set_perms.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/sethost.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/starttime.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/strlcpy_unesc.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/strlist.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/strvec_join.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/sudo_nss.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/sudoers.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/sudoers_cb.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/sudoers_ctx_free.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/sudoers_debug.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/timeout.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/timestamp.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/toke_util.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/src/copy_file.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/src/edit_open.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/src/exec.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/src/exec_common.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/src/exec_intercept.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/src/exec_iolog.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/src/exec_monitor.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/src/exec_nopty.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/src/exec_preload.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/src/exec_ptrace.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/src/exec_pty.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/src/get_pty.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/src/hooks.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/src/limits.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/src/load_plugins.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/src/net_ifs.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/src/parse_args.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/src/preserve_fds.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/src/signal.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/src/sudo.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/src/sudo_edit.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/src/suspend_parent.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/src/tgetpass.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/src/ttyname.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/src/utmp.c"

```
