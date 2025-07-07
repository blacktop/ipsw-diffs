## PosterBoardServices

> `/System/Library/PrivateFrameworks/PosterBoardServices.framework/PosterBoardServices`

```diff

-280.101.0.0.0
-  __TEXT.__text: 0x45748
+283.101.0.0.0
+  __TEXT.__text: 0x45704
   __TEXT.__auth_stubs: 0xa50
   __TEXT.__objc_methlist: 0x393c
   __TEXT.__const: 0x140
-  __TEXT.__cstring: 0x44bf
+  __TEXT.__cstring: 0x44c2
   __TEXT.__gcc_except_tab: 0x764
   __TEXT.__oslogstring: 0x159b
   __TEXT.__dlopen_cstrs: 0x203
   __TEXT.__unwind_info: 0xf48
   __TEXT.__objc_classname: 0x860
-  __TEXT.__objc_methname: 0x9e5e
-  __TEXT.__objc_methtype: 0x1a34
+  __TEXT.__objc_methname: 0x9e64
+  __TEXT.__objc_methtype: 0x1a0b
   __TEXT.__objc_stubs: 0x5d60
   __DATA_CONST.__got: 0x450
   __DATA_CONST.__const: 0x1118

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A62245F0-844A-3254-AD95-B035689592BF
+  UUID: CCF53F12-3C57-32A8-A757-30CD7EAF5039
   Functions: 1616
   Symbols:   5772
-  CStrings:  2692
+  CStrings:  2691
 
Symbols:
+ -[PRSServer deleteSnapshotsWithCompletion:]
+ -[PRSService deleteSnapshotsWithCompletion:]
+ -[PRSService deleteSnapshotsWithCompletion:].cold.1
+ ___44-[PRSService deleteSnapshotsWithCompletion:]_block_invoke
+ ___44-[PRSService deleteSnapshotsWithCompletion:]_block_invoke.cold.1
+ _objc_msgSend$deleteSnapshotsWithCompletion:
+ _objc_msgSend$server:deleteSnapshotsWithCompletion:
- -[PRSServer deleteSnapshots:completion:]
- -[PRSService deleteSnapshots:completion:]
- -[PRSService deleteSnapshots:completion:].cold.1
- ___41-[PRSService deleteSnapshots:completion:]_block_invoke
- ___41-[PRSService deleteSnapshots:completion:]_block_invoke.cold.1
- _objc_msgSend$deleteSnapshots:completion:
- _objc_msgSend$server:deleteSnapshots:completion:
CStrings:
+ "-[PRSServer deleteSnapshotsWithCompletion:]"
+ "deleteSnapshotsWithCompletion:"
+ "server:deleteSnapshotsWithCompletion:"
- "-[PRSServer deleteSnapshots:completion:]"
- "Vv32@0:8@\"NSNumber\"16@?<v@?@\"NSError\">24"
- "deleteSnapshots:completion:"
- "server:deleteSnapshots:completion:"

```
