## RunningBoard

> `/System/Library/PrivateFrameworks/RunningBoard.framework/RunningBoard`

```diff

-874.102.1.0.0
-  __TEXT.__text: 0x78c60
+874.122.2.0.0
+  __TEXT.__text: 0x79004
   __TEXT.__auth_stubs: 0x1420
   __TEXT.__objc_methlist: 0x4cd8
   __TEXT.__const: 0xd0
-  __TEXT.__cstring: 0x6927
-  __TEXT.__oslogstring: 0xaa95
-  __TEXT.__gcc_except_tab: 0x7b4
-  __TEXT.__unwind_info: 0x1958
+  __TEXT.__cstring: 0x695c
+  __TEXT.__oslogstring: 0xac58
+  __TEXT.__gcc_except_tab: 0x7e8
+  __TEXT.__unwind_info: 0x1a00
   __TEXT.__objc_classname: 0xea8
-  __TEXT.__objc_methname: 0xc83e
+  __TEXT.__objc_methname: 0xc858
   __TEXT.__objc_methtype: 0x2a76
   __TEXT.__objc_stubs: 0x9780
   __DATA_CONST.__got: 0x178
-  __DATA_CONST.__const: 0x1580
+  __DATA_CONST.__const: 0x15d0
   __DATA_CONST.__objc_classlist: 0x348
   __DATA_CONST.__objc_catlist: 0x158
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xb1b8
+  __DATA_CONST.__objc_const: 0xb1d8
   __DATA_CONST.__objc_selrefs: 0x2a00
   __DATA_CONST.__objc_classrefs: 0x6a8
   __DATA_CONST.__objc_superrefs: 0x280
   __DATA_CONST.__objc_arraydata: 0x678
-  __AUTH_CONST.__cfstring: 0x56e0
+  __AUTH_CONST.__cfstring: 0x5700
   __AUTH_CONST.__const: 0x5e0
   __AUTH_CONST.__objc_const: 0x3220
   __AUTH_CONST.__objc_intobj: 0x240

   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__auth_got: 0xa20
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x98c
-  __DATA.__data: 0x1200
-  __DATA.__bss: 0x50
+  __DATA.__objc_ivar: 0x990
+  __DATA.__data: 0x1210
+  __DATA.__bss: 0x30
   __DATA_DIRTY.__objc_data: 0x1ef0
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x230
+  __DATA_DIRTY.__bss: 0x23c
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libtailspin.dylib
   Functions: 2549
-  Symbols:   8863
-  CStrings:  4246
+  Symbols:   8866
+  CStrings:  4253
 
Symbols:
+ _OBJC_IVAR_$_RBProcessIndex._remainingStackshotsCount
+ ___45-[RBProcessIndex addProcess:existingProcess:]_block_invoke
+ ___80-[RBRequestManager executeLaunchRequest:euid:requestor:entitlements:completion:]_block_invoke.22
+ ___block_descriptor_56_e8_32s40s48s_e20_v20?0B8"NSError"12ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- -[RBProcessIndex addProcess:existingProcess:].cold.5
- ___80-[RBRequestManager executeLaunchRequest:euid:requestor:entitlements:completion:]_block_invoke_2
CStrings:
+ "Executing launch request for %{public}@ (%{public}@) from requestor: %{public}@"
+ "Existing process in RBProcessIndex is: %{public}@"
+ "Stackshot completed for processes %{public}@ and process %{public}@ which have different identities but the same identifier: %{public}@"
+ "Stackshot for unequal identies - processes %@ and %@"
+ "We already have an extension %@ with this pid: %d, were two launches for the same extension executed? Returning the existing instance."
+ "_remainingStackshotsCount"
+ "cannot map existing process %{public}@ and new process %{public}@ which have the same identifier: %{public}@"
+ "existingInstance is: %{public}@"
+ "existingProcess in RBProcessManager is: %{public}@"
+ "setting abstract target for %{public}@ to %{public}@"
- "We already have a process %@ with this identifier: %@, were two launches for the same process executed?"
- "cannot map two processes with the same identifier: %@"
- "setting abstract target for %@ to %@"

```
