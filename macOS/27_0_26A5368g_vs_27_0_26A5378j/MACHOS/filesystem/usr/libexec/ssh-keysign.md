## ssh-keysign

> `/usr/libexec/ssh-keysign`

```diff

-  __TEXT.__text: 0x1f008
+  __TEXT.__text: 0x1ef84
   __TEXT.__auth_stubs: 0xd70
   __TEXT.__const: 0x1bfb0
   __TEXT.__cstring: 0x512b
-  __TEXT.__unwind_info: 0x4c0
+  __TEXT.__unwind_info: 0x4b8
   __DATA_CONST.__const: 0x1d98
   __DATA_CONST.__auth_got: 0x6b8
   __DATA_CONST.__got: 0x38
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ sub_100000fd8 : 14380 -> 14388
~ sub_100005ad4 -> sub_100005adc : 1404 -> 1364
~ sub_10000661c -> sub_1000065fc : 176 -> 180
~ sub_10000a26c -> sub_10000a250 : 92 -> 76
~ sub_10000a2c8 -> sub_10000a29c : 228 -> 244
~ sub_10000e030 -> sub_10000e014 : 240 -> 228
~ sub_10000f5e0 -> sub_10000f5b8 : 1284 -> 1296
~ sub_10000fe14 -> sub_10000fdf8 : 64 -> 56
~ sub_10001bfb8 -> sub_10001bf94 : 440 -> 432
~ sub_10001dfec -> sub_10001dfc0 : 648 -> 652
~ sub_10001e8ec -> sub_10001e8c4 : 716 -> 700
~ sub_10001ebd0 -> sub_10001eb98 : 1456 -> 1412
~ sub_10001f180 -> sub_10001f11c : 164 -> 148
~ sub_10001f224 -> sub_10001f1b0 : 200 -> 184
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/addrmatch.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/canohost.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/entropy.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/kex-names.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/misc.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/msg.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/openbsd-compat/bsd-setres_id.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/readconf.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/readpass.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/ssh-ed25519-sk.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/ssh-ed25519.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/ssh-keysign.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/ssh-pkcs11.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/ssh-sk-client.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/ssherr-libcrypto.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/uidswap.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/xmalloc.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/addrmatch.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/canohost.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/entropy.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/kex-names.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/misc.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/msg.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/openbsd-compat/bsd-setres_id.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/readconf.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/readpass.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/ssh-ed25519-sk.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/ssh-ed25519.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/ssh-keysign.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/ssh-pkcs11.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/ssh-sk-client.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/ssherr-libcrypto.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/uidswap.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/xmalloc.c"

```
