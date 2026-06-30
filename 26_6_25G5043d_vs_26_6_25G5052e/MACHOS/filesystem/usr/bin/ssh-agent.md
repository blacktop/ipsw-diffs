## ssh-agent

> `/usr/bin/ssh-agent`

```diff

-354.160.4.0.0
+354.160.6.0.0
   __TEXT.__text: 0x18e70 sha256:86156c3ba1e1a7b6396e47a14311292ae5bc78066c2d98bc3668573540236534
   __TEXT.__auth_stubs: 0xc60 sha256:585599e594e2726002890640c146a46268f5ce0aed725e9635f70451449af5d7
-  __TEXT.__const: 0x1bf68 sha256:4ce79961a3f99b31eb0749fb413dd6af0e368b1771998c2762a2f5b6a4cba4ba
-  __TEXT.__cstring: 0x3cb6 sha256:19d65baae4cf253fcc42e769df308220ce4e4f519bdc2cf6c1e61b3cdc07b57c
+  __TEXT.__const: 0x1bf68 sha256:89343e50ee9bf795f3c3555214a56a9fb50dcdc8f4e460581f1d2f636da13539
+  __TEXT.__cstring: 0x3cb6 sha256:0d7694b6312b70d9f06cd537d1bea3e9db05757c24a919a6f5c5447591537488
   __TEXT.__unwind_info: 0x400 sha256:244db2985ca1fb7a8b0bbd6b7182aa912c2ce223edbbeca63609c34f6e2577dc
   __DATA_CONST.__auth_got: 0x630 sha256:a340cb685badb6fb69e21b0b0a76066da643003ba3fabc6f6e8a33d360fdc562
   __DATA_CONST.__got: 0x48 sha256:652b711c65440653080cdf60907bdb6bd069d8d62dbeb30798c784fd3b14bcbd

   - /usr/lib/libpam.2.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  UUID: FADF584B-6639-3D37-A3CF-6A2D15D1E668
+  UUID: 974F29A3-8EEF-3894-89AC-AD71A55DBC69
   Functions: 318
   Symbols:   218
   CStrings:  587
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/entropy.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/misc-agent.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/misc.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/msg.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/platform-tracing.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/readpass.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/ssh-agent.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/ssh-ed25519-sk.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/ssh-ed25519.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/ssh-pkcs11-client.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/ssh-sk-client.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/ssherr-libcrypto.c"
+ "/AppleInternal/Library/BuildRoots/4~CSWGugATBZUQO45Qhx0seZ_YXUwNYOUBw_rz91o/Library/Caches/com.apple.xbs/TemporaryDirectory.dlmV6r/Sources/OpenSSH/openssh/xmalloc.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/entropy.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/misc-agent.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/misc.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/msg.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/platform-tracing.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/readpass.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/ssh-agent.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/ssh-ed25519-sk.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/ssh-ed25519.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/ssh-pkcs11-client.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/ssh-sk-client.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/ssherr-libcrypto.c"
- "/AppleInternal/Library/BuildRoots/4~CRUjugAUieGf-dOI_SKop9adAJ52RdKFc-f23WE/Library/Caches/com.apple.xbs/TemporaryDirectory.DXT91L/Sources/OpenSSH/openssh/xmalloc.c"

```
