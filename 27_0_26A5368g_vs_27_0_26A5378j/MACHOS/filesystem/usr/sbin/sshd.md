## sshd

> `/usr/sbin/sshd`

```diff

-  __TEXT.__text: 0x2490c
+  __TEXT.__text: 0x248ac
   __TEXT.__auth_stubs: 0xf30
-  __TEXT.__const: 0x1bfc8
+  __TEXT.__const: 0x1bfd8
   __TEXT.__cstring: 0x6359
-  __TEXT.__unwind_info: 0x590
+  __TEXT.__unwind_info: 0x588
   __DATA_CONST.__const: 0x1b30
   __DATA_CONST.__auth_got: 0x798
   __DATA_CONST.__got: 0x50
Sections:
~ __TEXT.__cstring : content changed
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ sub_10000965c : 432 -> 440
~ sub_10000b690 -> sub_10000b698 : 7048 -> 7024
~ sub_10000ded4 -> sub_10000dec4 : 5620 -> 5644
~ sub_100010ee0 -> sub_100010ee8 : 92 -> 76
~ sub_100010f3c -> sub_100010f34 : 228 -> 244
~ sub_100015088 -> sub_100015090 : 240 -> 228
~ sub_100016444 -> sub_100016440 : 1284 -> 1296
~ sub_100016d80 -> sub_100016d88 : 64 -> 56
~ sub_100021840 : 440 -> 432
~ sub_1000233c8 -> sub_1000233c0 : 648 -> 652
~ sub_100023cc8 -> sub_100023cc4 : 716 -> 700
~ sub_100023fac -> sub_100023f98 : 1456 -> 1412
~ sub_10002455c -> sub_10002451c : 164 -> 148
~ sub_100024600 -> sub_1000245b0 : 200 -> 184
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/addrmatch.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/auth2-methods.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/authfd.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/authfile.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/canohost.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/entropy.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/groupaccess.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/kex-names.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/misc.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/servconf.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/srclimit.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/ssh-ed25519-sk.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/ssh-ed25519.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/sshd.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/ssherr-libcrypto.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/xmalloc.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/addrmatch.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/auth2-methods.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/authfd.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/authfile.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/canohost.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/entropy.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/groupaccess.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/kex-names.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/misc.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/servconf.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/srclimit.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/ssh-ed25519-sk.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/ssh-ed25519.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/sshd.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/ssherr-libcrypto.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/xmalloc.c"

```
