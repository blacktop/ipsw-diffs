## sshd-auth

> `/usr/libexec/sshd-auth`

```diff

-354.160.4.0.0
+354.160.6.0.0
   __TEXT.__text: 0x3ea84 sha256:35f9d47c55975d0357d0fcfc49583d4fd3ee6e248f2a4afdbaf7ddfbe90ee76a
   __TEXT.__auth_stubs: 0x11d0 sha256:ff74fb94570ffb87a5704f75aabc3dca4f6ac7ff661fce46949c8603841dfd7a
-  __TEXT.__const: 0x1b268 sha256:aaabbf51922c026479db9ef6bd00fb258332a06e4d94a13b494fe74c797185c3
-  __TEXT.__cstring: 0xc16e sha256:4b7d3eaa10b391d88eb7e79a1a6576d5cfdd696bf7536a518ac7b3e3ba027241
+  __TEXT.__const: 0x1b268 sha256:af631eb31bed6b9fb277e7d2e014fcdefaa6f0a24efbbabb0222479efbc7698f
+  __TEXT.__cstring: 0xc16e sha256:ffd833ea03372abe7a3829a0dba65d25ff1aa0cee974ce073f0f12b8e7c0f372
   __TEXT.__unwind_info: 0x948 sha256:2452c63e8157e146938814dbb90a14403e8731d14f88a2e8b40b3c0c61b9964a
   __TEXT.__eh_frame: 0xa0 sha256:c772362a05e07ee85515c459975aebef1d52b16b44b09a3842d8f625a333cd65
   __DATA_CONST.__auth_got: 0x8e8 sha256:a8e1e2cc23dcc9141221e95bcc03ee504aa1b1137da88c5d62f234734e2e5257

   - /usr/lib/libpam.2.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  UUID: F448A486-8F19-383F-AA21-C0315A2E1709
+  UUID: B80D7DF3-1C45-3D6E-BB2D-C03C8695458E
   Functions: 747
   Symbols:   318
   CStrings:  1656
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/EndpointSecurity/submit-ess-event.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/addrmatch.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/audit-bsm.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/auth-krb5.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/auth.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/auth2-chall.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/auth2-gss.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/auth2-hostbased.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/auth2-kbdint.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/auth2-methods.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/auth2-none.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/auth2-passwd.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/auth2-pubkey.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/auth2.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/authfd.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/canohost.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/channels.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/compat.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/dh.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/dispatch.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/entropy.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/groupaccess.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/gss-genr.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/gss-serv-krb5.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/kex-names.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/kex.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/kexgen.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/kexgexs.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/libcrux_mlkem768_sha3.h"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/misc.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/monitor_wrap.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/nchan.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/openbsd-compat/bsd-setres_id.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/packet.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/sandbox-darwin.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/servconf.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/ssh-ed25519-sk.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/ssh-ed25519.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/sshd-auth.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/ssherr-libcrypto.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/uidswap.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/xmalloc.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/EndpointSecurity/submit-ess-event.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/addrmatch.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/audit-bsm.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/auth-krb5.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/auth.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/auth2-chall.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/auth2-gss.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/auth2-hostbased.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/auth2-kbdint.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/auth2-methods.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/auth2-none.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/auth2-passwd.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/auth2-pubkey.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/auth2.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/authfd.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/canohost.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/channels.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/compat.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/dh.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/dispatch.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/entropy.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/groupaccess.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/gss-genr.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/gss-serv-krb5.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/kex-names.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/kex.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/kexgen.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/kexgexs.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/libcrux_mlkem768_sha3.h"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/misc.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/monitor_wrap.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/nchan.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/openbsd-compat/bsd-setres_id.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/packet.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/sandbox-darwin.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/servconf.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/ssh-ed25519-sk.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/ssh-ed25519.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/sshd-auth.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/ssherr-libcrypto.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/uidswap.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/xmalloc.c"

```
