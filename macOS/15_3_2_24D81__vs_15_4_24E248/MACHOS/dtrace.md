## dtrace

> `/usr/sbin/dtrace`

```diff

 411.0.0.0.0
-  __TEXT.__text: 0x3808
+  __TEXT.__text: 0x37c4
   __TEXT.__auth_stubs: 0x520
-  __TEXT.__cstring: 0x16d3
   __TEXT.__const: 0x4d
+  __TEXT.__cstring: 0x16cc
   __TEXT.__unwind_info: 0xd8
   __DATA_CONST.__auth_got: 0x290
   __DATA_CONST.__got: 0x58

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libdtrace.dylib
-  UUID: EF4F057D-9BBE-32C6-8A2E-8A704E94E3B6
-  Functions: 28
+  UUID: 51973F75-8E2A-314E-8E7E-14640EDA5D0E
+  Functions: 27
   Symbols:   154
-  CStrings:  215
+  CStrings:  212
 
Functions:
~ _main : 7080 -> 7084
- sub_100004784
~ _notice : 56 -> 64
~ _dfatal : 308 -> 280
~ _go : 836 -> 868
~ _chewrec : 92 -> 104
~ _chew : 644 -> 636
~ _info_stmt : 152 -> 148
~ _bufhandler : 2064 -> 2000
CStrings:
- ".d"
- "2"
- "4"

```
