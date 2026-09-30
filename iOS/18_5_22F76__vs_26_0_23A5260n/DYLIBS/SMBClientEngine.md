## SMBClientEngine

> `/System/Library/PrivateFrameworks/SMBClientEngine.framework/SMBClientEngine`

```diff

-147.0.0.0.0
-  __TEXT.__text: 0x36968
+150.0.0.0.0
+  __TEXT.__text: 0x36bac
   __TEXT.__auth_stubs: 0xc40
   __TEXT.__objc_methlist: 0xeb0
   __TEXT.__const: 0x7b0
   __TEXT.__gcc_except_tab: 0xa40
-  __TEXT.__oslogstring: 0x45e0
-  __TEXT.__cstring: 0x19af
+  __TEXT.__oslogstring: 0x4627
+  __TEXT.__cstring: 0x1a06
   __TEXT.__unwind_info: 0x6b8
   __TEXT.__objc_classname: 0xa7
-  __TEXT.__objc_methname: 0x2950
+  __TEXT.__objc_methname: 0x2963
   __TEXT.__objc_methtype: 0x1f15
   __TEXT.__objc_stubs: 0x1cc0
   __DATA_CONST.__got: 0xe8

   __AUTH_CONST.__auth_got: 0x630
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x180
-  __AUTH_CONST.__objc_const: 0x1d98
+  __AUTH_CONST.__objc_const: 0x1dd8
   __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0x248
+  __DATA.__objc_ivar: 0x250
   __DATA.__data: 0x1a
   __DATA.__common: 0x4
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/Heimdal.framework/Heimdal
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libheimdal-asn1.dylib
-  - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FA6F6C90-5B54-3675-928A-7B83D4BC6D36
-  Functions: 1260
-  Symbols:   3281
-  CStrings:  1419
+  UUID: 445CCD07-6EB2-3D45-871F-C3D7243EC2E0
+  Functions: 1262
+  Symbols:   3287
+  CStrings:  1424
 
Symbols:
+ -[SMBDirEnumerator commonInit:onShareID:dirName:lookUpName:searchFlags:outParameters:].cold.1
+ -[SMBDirEnumerator smb2fs_smb_findnext:].cold.6
+ _OBJC_IVAR_$_SMBDirEnumerator.f_dir_lock
+ _OBJC_IVAR_$_SMBDirEnumerator.f_state
Functions:
~ -[SMBDirEnumerator cleanup] : 260 -> 304
~ -[SMBDirEnumerator dealloc] : 72 -> 100
~ -[SMBDirEnumerator commonInit:onShareID:dirName:lookUpName:searchFlags:outParameters:] : 272 -> 344
~ -[SMBDirEnumerator nextEntry:outParameters:callBack:] : 444 -> 468
~ ___53-[SMBDirEnumerator nextEntry:outParameters:callBack:]_block_invoke : 688 -> 788
~ -[SMBDirEnumerator smb2fs_smb_findnext:] : 1040 -> 1072
~ _smb2_smb_create : 3388 -> 3392
~ ___piston_negotiate_block_invoke : 1816 -> 1824
~ ___piston_negotiate_block_invoke.9 : 1476 -> 1488
+ -[SMBDirEnumerator commonInit:onShareID:dirName:lookUpName:searchFlags:outParameters:].cold.1
+ -[SMBDirEnumerator smb2_smb_parse_query_dir_both_dir_info:].cold.29
CStrings:
+ "%s: mdp is null? \n"
+ "%s: pthread_mutex_init failed for f_dir_lock <%d> \n"
+ "-[SMBDirEnumerator commonInit:onShareID:dirName:lookUpName:searchFlags:outParameters:]"
+ "f_dir_lock"
+ "f_state"

```
