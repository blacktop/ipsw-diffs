## managedappdistributiond

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond`

```diff

-3.1.3.0.0
-  __TEXT.__text: 0x630c3c
-  __TEXT.__auth_stubs: 0x6000
+3.1.8.0.0
+  __TEXT.__text: 0x639fa4
+  __TEXT.__auth_stubs: 0x6020
   __TEXT.__objc_stubs: 0x1a80
   __TEXT.__objc_methlist: 0x218c
-  __TEXT.__const: 0x3c814
+  __TEXT.__const: 0x3ca94
   __TEXT.__swift5_entry: 0x8
   __TEXT.__objc_methname: 0x61c1
-  __TEXT.__cstring: 0xc6d5
-  __TEXT.__oslogstring: 0xf182
+  __TEXT.__cstring: 0xcd35
+  __TEXT.__oslogstring: 0xf282
   __TEXT.__objc_classname: 0x3e9
   __TEXT.__objc_methtype: 0x150c
-  __TEXT.__gcc_except_tab: 0x508
+  __TEXT.__gcc_except_tab: 0x50c
   __TEXT.__dlopen_cstrs: 0xc8
-  __TEXT.__constg_swiftt: 0x6630
-  __TEXT.__swift5_typeref: 0x5882
+  __TEXT.__constg_swiftt: 0x66a4
+  __TEXT.__swift5_typeref: 0x58b6
   __TEXT.__swift5_proto: 0x1728
-  __TEXT.__swift5_types: 0x930
-  __TEXT.__swift_as_entry: 0x9f0
-  __TEXT.__swift_as_ret: 0x1280
+  __TEXT.__swift5_types: 0x934
+  __TEXT.__swift_as_entry: 0xa48
+  __TEXT.__swift_as_ret: 0x133c
   __TEXT.__swift5_protos: 0xa4
-  __TEXT.__unwind_info: 0x10f08
-  __TEXT.__eh_frame: 0x343dc
-  __DATA_CONST.__auth_got: 0x3010
-  __DATA_CONST.__got: 0x1cf0
-  __DATA_CONST.__auth_ptr: 0x17b8
-  __DATA_CONST.__const: 0x2d730
+  __TEXT.__unwind_info: 0x11530
+  __TEXT.__eh_frame: 0x35124
+  __DATA_CONST.__auth_got: 0x3020
+  __DATA_CONST.__got: 0x1d00
+  __DATA_CONST.__auth_ptr: 0x17c0
+  __DATA_CONST.__const: 0x2d950
   __DATA_CONST.__cfstring: 0xae0
   __DATA_CONST.__objc_classlist: 0x2d0
   __DATA_CONST.__objc_protolist: 0x160

   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x5ec8
+  __DATA.__objc_const: 0x5fb0
   __DATA.__objc_selrefs: 0x1c38
   __DATA.__objc_ivar: 0xcc
   __DATA.__objc_data: 0x1f30
-  __DATA.__data: 0xcfc8
+  __DATA.__data: 0xd0b0
   __DATA.__bss: 0x2cc50
   __DATA.__common: 0xcb0
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A656E97C-7485-3B8A-8C15-0736FCB52041
-  Functions: 14947
-  Symbols:   2885
-  CStrings:  3809
+  UUID: E6BC6356-48B8-31C6-8FDE-882D99062AF5
+  Functions: 15068
+  Symbols:   2889
+  CStrings:  3839
 
Symbols:
+ _$s22ManagedAppDistribution05StoreB10IdentifierOSHAAMc
+ _$s22ManagedAppDistribution0aB11DeclarationV15ManagementScopeO2eeoiySbAE_AEtFZ
+ _$s22ManagedAppDistribution0aB11DeclarationV15ManagementScopeO4hash4intoys6HasherVz_tF
+ _$syycWV
CStrings:
+ "@@requestor@@ asked for an exception to get “@@appName@@” from “@@source@@”. It's rated @@rating@@ and restricted on their device."
+ "Approve in Person"
+ "Ask for Exception"
+ "Ask your parent or guardian for an exception to get this app from the web"
+ "Ask your parent or guardian for an exception to get this app from “@@source@@”."
+ "ManagedAppDistribution.AskForException.Button.ApproveInPerson"
+ "ManagedAppDistribution.AskForException.Button.Ask"
+ "ManagedAppDistribution.AskForException.Prompt.Body.Marketplace"
+ "ManagedAppDistribution.AskForException.Prompt.Body.Web"
+ "ManagedAppDistribution.AskForException.Prompt.Sent.Body"
+ "ManagedAppDistribution.AskForException.Prompt.Title.Marketplace"
+ "ManagedAppDistribution.AskForException.Prompt.Title.Web"
+ "ManagedAppDistribution.AskForException.Request.Message.Body"
+ "ManagedAppDistribution.AskForException.Request.Message.Title"
+ "ManagedAppDistribution.Common.Close"
+ "Post declaration removal state change"
+ "Request from @@requestor@@"
+ "Your content restrictions are enabled. Updates and purchases in this app will be managed by the developer “@@developer@@”. Verify the information below before installing."
+ "Your content restrictions are enabled. Updates and purchases in this app will be managed by “@@marketplaceName@@”. Verify the information below before installing."
+ "Your request was sent and is awaiting approval from a parent or a guardian. They can also approve in person on this device."
+ "[%@] Error when posting state changes: %{public}@"
+ "[%@] Failed to send refresh metadata for %ld app(s): %{public}@"
+ "[%@] Sending updated metadata for %ld app(s) to clients"
+ "[%@] Unable to remove install history: %{public}@"
+ "duration"
+ "handler"
+ "postTimer"
+ "statePostTimer"
+ "stateRemovalTimer"
+ "task"

```
