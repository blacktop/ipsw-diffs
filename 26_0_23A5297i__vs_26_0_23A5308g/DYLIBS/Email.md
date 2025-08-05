## Email

> `/System/Library/PrivateFrameworks/Email.framework/Email`

```diff

-3860.100.5.2.1
-  __TEXT.__text: 0xcb7a0
+3863.100.1.2.5
+  __TEXT.__text: 0xcc1b0
   __TEXT.__auth_stubs: 0x14e0
   __TEXT.__objc_methlist: 0xc6fc
-  __TEXT.__gcc_except_tab: 0x1aa78
-  __TEXT.__const: 0x11a8
-  __TEXT.__cstring: 0xb43c
-  __TEXT.__oslogstring: 0x5e63
+  __TEXT.__gcc_except_tab: 0x1ac1c
+  __TEXT.__const: 0x11b8
+  __TEXT.__cstring: 0xb42c
+  __TEXT.__oslogstring: 0x6023
   __TEXT.__dlopen_cstrs: 0x10a
   __TEXT.__ustring: 0x154
   __TEXT.__constg_swiftt: 0x3e8

   __TEXT.__swift5_capture: 0x38
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x78c8
+  __TEXT.__unwind_info: 0x78d0
   __TEXT.__eh_frame: 0x1f8
   __TEXT.__objc_classname: 0x1a20
   __TEXT.__objc_methname: 0x1a8e7

   __DATA_CONST.__objc_superrefs: 0x470
   __DATA_CONST.__objc_arraydata: 0x1d0
   __AUTH_CONST.__auth_got: 0xa80
-  __AUTH_CONST.__const: 0x1808
+  __AUTH_CONST.__const: 0x1828
   __AUTH_CONST.__cfstring: 0x9a00
   __AUTH_CONST.__objc_const: 0x15f18
   __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x5a0
-  __AUTH.__data: 0x200
+  __AUTH.__objc_data: 0x618
+  __AUTH.__data: 0x158
   __DATA.__objc_ivar: 0xba4
-  __DATA.__data: 0x2888
-  __DATA.__bss: 0x1da0
-  __DATA_DIRTY.__objc_data: 0x3228
-  __DATA_DIRTY.__data: 0xd0
-  __DATA_DIRTY.__bss: 0x630
+  __DATA.__data: 0x2898
+  __DATA.__bss: 0x1b80
+  __DATA_DIRTY.__objc_data: 0x31b0
+  __DATA_DIRTY.__data: 0x1e0
+  __DATA_DIRTY.__bss: 0x860
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 80A11DD1-44E5-325B-B459-C87F2743C5C2
-  Functions: 4702
-  Symbols:   17474
-  CStrings:  8285
+  UUID: 60CD3A47-51CD-33E2-935E-D23A0108A98D
+  Functions: 4706
+  Symbols:   17484
+  CStrings:  8296
 
Symbols:
+ -[_EMMessageRepositoryQueryObserver observer:matchedChangesForObjectIDs:].cold.1
+ ____ef_log_EMBlockedSenderManager_block_invoke
+ __ef_log_EMBlockedSenderManager
+ __ef_log_EMBlockedSenderManager.cold.1
+ __ef_log_EMBlockedSenderManager.log
+ __ef_log_EMBlockedSenderManager.onceToken
CStrings:
+ "%p: %{public}@ is blocked in list (%lu)"
+ "%p: Block email address: %{public}@"
+ "%p: Block phone number"
+ "%p: Is %{public}@ blocked=%{BOOL}d"
+ "%p: Unblock email address: %{public}@"
+ "%p: Unblock phone number"
+ "%p: Update Blocked Sender List - New Blocked Senders=%lu, Previous Blocked Senders=%lu, Block List Count=%lu"
+ "%p: Update Blocked Senders Enabled=%{BOOL}d"
+ "%p: Update Move To Trash=%{BOOL}d"
+ "<%{public}@> dropping notification due to nil trampoliningObserver"
+ "EMBusinessExternalID.m"
+ "EMCategory.m"
+ "EMGroupedSender.m"
+ "EMGroupedSenderObjectID.m"
- "EMBusinessExternalID-BlackPearl.m"
- "EMCategory-BlackPearl.m"
- "EMGroupedSender-BlackPearlUI.m"
- "EMGroupedSenderObjectID-BlackPearlUI.m"

```
