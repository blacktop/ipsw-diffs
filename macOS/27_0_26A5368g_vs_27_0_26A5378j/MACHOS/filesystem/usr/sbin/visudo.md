## visudo

> `/usr/sbin/visudo`

```diff

-  __TEXT.__text: 0x2a0c0
+  __TEXT.__text: 0x2a080
   __TEXT.__auth_stubs: 0x8d0
   __TEXT.__cstring: 0x81a8
   __TEXT.__const: 0xc7e0
Sections:
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ sub_1000010ac : 1108 -> 1112
~ sub_100009510 -> sub_100009514 : 364 -> 348
~ sub_100009c58 -> sub_100009c4c : 304 -> 292
~ sub_10000b454 -> sub_10000b43c : 5940 -> 5928
~ sub_1000110a4 -> sub_100011080 : 4856 -> 4888
~ sub_100019150 -> sub_10001914c : 15272 -> 15256
~ sub_10001dd3c -> sub_10001dd28 : 4512 -> 4500
~ sub_10001eee8 -> sub_10001eec8 : 340 -> 328
~ sub_10001f9b0 -> sub_10001f984 : 264 -> 256
~ sub_100020f98 -> sub_100020f64 : 932 -> 924
~ sub_10002185c -> sub_100021820 : 860 -> 868
~ sub_100022258 -> sub_100022224 : 256 -> 272
~ sub_100022470 -> sub_10002244c : 256 -> 272
~ sub_10002351c -> sub_100023508 : 2840 -> 2832
~ sub_100025e68 -> sub_100025e4c : 684 -> 672
~ sub_10002635c -> sub_100026334 : 1820 -> 1824
~ sub_100026de4 -> sub_100026dc0 : 652 -> 620
~ sub_100027070 -> sub_10002702c : 916 -> 892
~ sub_100027404 -> sub_1000273a8 : 496 -> 520
~ sub_1000281cc -> sub_100028188 : 316 -> 320
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/digest.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/getgrouplist.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/gettime.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/hexchar.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/lbuf.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/locking.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/logfac.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/logpri.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/parseln.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/rcstr.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/regex.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/secure_path.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/strsplit.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/strtobool.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/strtoid.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/strtomode.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/sudo_conf.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/lib/util/term.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/alias.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/b64_decode.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/canon_path.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/check_aliases.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/defaults.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/digestname.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/editor.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/filedigest.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/find_path.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/gentime.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/goodpath.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/locale.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/match.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/match_addr.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/match_command.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/match_digest.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/parser_warnx.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/pwutil.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/pwutil_impl.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/redblack.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/sethost.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/sudoers_ctx_free.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/sudoers_debug.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/timeout.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/toke_util.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/visudo.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.P1Y8z7/Sources/sudo/sudo/plugins/sudoers/visudo_cb.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/digest.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/getgrouplist.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/gettime.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/hexchar.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/lbuf.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/locking.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/logfac.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/logpri.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/parseln.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/rcstr.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/regex.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/secure_path.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/strsplit.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/strtobool.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/strtoid.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/strtomode.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/sudo_conf.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/lib/util/term.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/alias.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/b64_decode.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/canon_path.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/check_aliases.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/defaults.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/digestname.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/editor.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/filedigest.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/find_path.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/gentime.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/goodpath.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/locale.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/match.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/match_addr.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/match_command.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/match_digest.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/parser_warnx.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/pwutil.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/pwutil_impl.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/redblack.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/sethost.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/sudoers_ctx_free.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/sudoers_debug.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/timeout.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/toke_util.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/visudo.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Qdai0V/Sources/sudo/sudo/plugins/sudoers/visudo_cb.c"

```
