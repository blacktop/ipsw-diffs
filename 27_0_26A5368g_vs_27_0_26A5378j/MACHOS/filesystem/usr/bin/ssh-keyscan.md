## ssh-keyscan

> `/usr/bin/ssh-keyscan`

```diff

-  __TEXT.__text: 0x22c50
+  __TEXT.__text: 0x22c54
   __TEXT.__auth_stubs: 0xcb0
-  __TEXT.__const: 0x1b1f8
+  __TEXT.__const: 0x1b208
   __TEXT.__cstring: 0x4f03
-  __TEXT.__unwind_info: 0x570
+  __TEXT.__unwind_info: 0x580
   __TEXT.__eh_frame: 0xa0
   __DATA_CONST.__const: 0xf78
   __DATA_CONST.__auth_got: 0x658
Sections:
~ __TEXT.__cstring : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
Functions:
~ sub_1000050ac : 1292 -> 1296
~ sub_100007614 -> sub_100007618 : 4884 -> 4888
~ sub_10000a3c8 -> sub_10000a3d0 : 92 -> 76
~ sub_100012b18 -> sub_100012b10 : 252 -> 260
~ sub_100012f50 : 240 -> 228
~ sub_100013e24 -> sub_100013e18 : 64 -> 56
~ sub_100017610 -> sub_1000175fc : 76 -> 92
~ sub_10001765c -> sub_100017658 : 80 -> 96
~ sub_1000176ac -> sub_1000176b8 : 80 -> 96
~ sub_100018340 -> sub_10001835c : 2000 -> 2004
~ sub_100021548 -> sub_100021568 : 152 -> 124
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/canohost.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/compat.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/dh.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/dispatch.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/dns.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/entropy.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/hostfile.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/kex.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/kexgen.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/kexgexc.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/libcrux_mlkem768_sha3.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/misc.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/packet.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/ssh-ed25519-sk.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/ssh-ed25519.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/ssh-keyscan.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/ssherr-libcrypto.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5ygCjQ/Sources/OpenSSH/openssh/xmalloc.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/canohost.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/compat.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/dh.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/dispatch.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/dns.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/entropy.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/hostfile.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/kex.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/kexgen.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/kexgexc.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/libcrux_mlkem768_sha3.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/misc.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/packet.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/ssh-ed25519-sk.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/ssh-ed25519.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/ssh-keyscan.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/ssherr-libcrypto.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.KttaKD/Sources/OpenSSH/openssh/xmalloc.c"

```
