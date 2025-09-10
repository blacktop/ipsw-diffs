## RunningBoard

> `/System/Library/PrivateFrameworks/RunningBoard.framework/RunningBoard`

```diff

 1008.0.2.0.0
-  __TEXT.__text: 0x7db04
+  __TEXT.__text: 0x7dbe0
   __TEXT.__auth_stubs: 0x14a0
   __TEXT.__objc_methlist: 0x61b4
   __TEXT.__const: 0x1f8
-  __TEXT.__cstring: 0x7c24
-  __TEXT.__oslogstring: 0xb539
+  __TEXT.__cstring: 0x7c3d
+  __TEXT.__oslogstring: 0xb560
   __TEXT.__gcc_except_tab: 0xcbc
   __TEXT.__unwind_info: 0x1b48
   __TEXT.__objc_classname: 0xf7c

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 304B4362-CC96-3F11-9D6B-F1FFFDDBCBF7
+  UUID: 1C828B19-0D15-3B7B-8954-7C2F9A1FE474
   Functions: 2719
   Symbols:   9483
-  CStrings:  5430
+  CStrings:  5432
 
Symbols:
+ ___60-[RBLaunchdJobManager invokeOnProcessDeath:handler:onQueue:]_block_invoke.199
+ ___63-[RBLaunchdJobManager _createAndSubmitExtensionJob:UUID:error:]_block_invoke.151
- ___60-[RBLaunchdJobManager invokeOnProcessDeath:handler:onQueue:]_block_invoke.198
- ___63-[RBLaunchdJobManager _createAndSubmitExtensionJob:UUID:error:]_block_invoke.150
Functions:
~ __addRBProperties : 1104 -> 1216
~ -[RBLaunchdJobManager _addAppPropertiesToData:forIdentity:context:actualIdentity:error:] : 2960 -> 3068
CStrings:
+ "EnableCheckedAllocations"
+ "Launching %{public}@ with MTE enabled."

```
