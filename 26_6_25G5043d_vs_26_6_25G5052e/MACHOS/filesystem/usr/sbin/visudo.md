## visudo

> `/usr/sbin/visudo`

```diff

 114.100.11.0.0
   __TEXT.__text: 0x29ca4 sha256:36009698ba4b2acbcf8617ef9d87a81868cdd3f41b0921ac93c5faa68349e89f
   __TEXT.__auth_stubs: 0x8d0 sha256:39cd30f548f38c618d435d5b057170a43b37cdf4f8e63fb95c6285ffba5c7f81
-  __TEXT.__cstring: 0x81a8 sha256:2354e724e0850710021189205e1a5cb9e87d359f0d2ef3bbf8cbc5182765a02a
+  __TEXT.__cstring: 0x81a8 sha256:fc6ca3a88a4dc66e4a511ddebfbd10748b4e66c019d12a9d79f11b8a8607dcde
   __TEXT.__const: 0xc7e0 sha256:80375a985cf31876e315f032152fbcb6a87afc08e22521d910677ea8e768712c
   __TEXT.__oslogstring: 0x5c sha256:af3a78b2cd997efe3f904ea731af7e05fa65227dc7184d923099b756916289a7
   __TEXT.__unwind_info: 0x4b8 sha256:e2907a750cffa1f5a13d90c6eccb9eee8c392ef430556db9ec61277923c91639

   - /usr/lib/libEndpointSecuritySystem.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libpam.2.dylib
-  UUID: F9B03487-74D6-3FCE-B542-2BFDF98DDA23
+  UUID: 58E7D832-715E-325E-B3E1-238F6BBC024C
   Functions: 441
   Symbols:   152
   CStrings:  1199
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/lib/util/digest.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/lib/util/getgrouplist.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/lib/util/gettime.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/lib/util/hexchar.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/lib/util/lbuf.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/lib/util/locking.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/lib/util/logfac.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/lib/util/logpri.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/lib/util/parseln.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/lib/util/rcstr.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/lib/util/regex.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/lib/util/secure_path.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/lib/util/strsplit.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/lib/util/strtobool.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/lib/util/strtoid.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/lib/util/strtomode.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/lib/util/sudo_conf.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/lib/util/term.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/plugins/sudoers/alias.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/plugins/sudoers/b64_decode.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/plugins/sudoers/canon_path.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/plugins/sudoers/check_aliases.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/plugins/sudoers/defaults.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/plugins/sudoers/digestname.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/plugins/sudoers/editor.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/plugins/sudoers/filedigest.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/plugins/sudoers/find_path.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/plugins/sudoers/gentime.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/plugins/sudoers/goodpath.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/plugins/sudoers/locale.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/plugins/sudoers/match.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/plugins/sudoers/match_addr.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/plugins/sudoers/match_command.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/plugins/sudoers/match_digest.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/plugins/sudoers/parser_warnx.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/plugins/sudoers/pwutil.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/plugins/sudoers/pwutil_impl.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/plugins/sudoers/redblack.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/plugins/sudoers/sethost.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/plugins/sudoers/sudoers_ctx_free.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/plugins/sudoers/sudoers_debug.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/plugins/sudoers/timeout.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/plugins/sudoers/toke_util.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/plugins/sudoers/visudo.c"
+ "/AppleInternal/Library/BuildRoots/4~CR_2ugChhO1xi4QiPaxRApjaBBvCTWv1nrc1mbM/Library/Caches/com.apple.xbs/TemporaryDirectory.4iEyYo/Sources/sudo/sudo/plugins/sudoers/visudo_cb.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/lib/util/digest.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/lib/util/getgrouplist.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/lib/util/gettime.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/lib/util/hexchar.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/lib/util/lbuf.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/lib/util/locking.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/lib/util/logfac.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/lib/util/logpri.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/lib/util/parseln.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/lib/util/rcstr.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/lib/util/regex.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/lib/util/secure_path.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/lib/util/strsplit.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/lib/util/strtobool.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/lib/util/strtoid.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/lib/util/strtomode.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/lib/util/sudo_conf.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/lib/util/term.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/plugins/sudoers/alias.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/plugins/sudoers/b64_decode.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/plugins/sudoers/canon_path.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/plugins/sudoers/check_aliases.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/plugins/sudoers/defaults.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/plugins/sudoers/digestname.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/plugins/sudoers/editor.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/plugins/sudoers/filedigest.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/plugins/sudoers/find_path.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/plugins/sudoers/gentime.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/plugins/sudoers/goodpath.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/plugins/sudoers/locale.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/plugins/sudoers/match.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/plugins/sudoers/match_addr.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/plugins/sudoers/match_command.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/plugins/sudoers/match_digest.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/plugins/sudoers/parser_warnx.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/plugins/sudoers/pwutil.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/plugins/sudoers/pwutil_impl.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/plugins/sudoers/redblack.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/plugins/sudoers/sethost.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/plugins/sudoers/sudoers_ctx_free.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/plugins/sudoers/sudoers_debug.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/plugins/sudoers/timeout.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/plugins/sudoers/toke_util.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/plugins/sudoers/visudo.c"
- "/AppleInternal/Library/BuildRoots/4~CQ4fugBz4slOreezvcfB8qpzmN7wfv0IZktCyFQ/Library/Caches/com.apple.xbs/TemporaryDirectory.3CRfFC/Sources/sudo/sudo/plugins/sudoers/visudo_cb.c"

```
