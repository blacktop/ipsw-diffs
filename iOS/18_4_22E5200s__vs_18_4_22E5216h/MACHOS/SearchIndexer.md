## SearchIndexer

> `/System/Library/PrivateFrameworks/Message.framework/XPCServices/SearchIndexer.xpc/SearchIndexer`

```diff

-3826.500.135.2.7
-  __TEXT.__text: 0x4d4638
+3826.500.166.2.2
+  __TEXT.__text: 0x4df784
   __TEXT.__auth_stubs: 0x4430
   __TEXT.__objc_stubs: 0x140
   __TEXT.__objc_methlist: 0x684
-  __TEXT.__cstring: 0x8d69
+  __TEXT.__cstring: 0x8d39
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x59e98
-  __TEXT.__swift5_typeref: 0xe025
+  __TEXT.__const: 0x59d98
+  __TEXT.__swift5_typeref: 0xe031
   __TEXT.__swift5_capture: 0x8164
-  __TEXT.__constg_swiftt: 0xb7cc
+  __TEXT.__constg_swiftt: 0xb7b8
   __TEXT.__swift5_reflstr: 0xd479
-  __TEXT.__swift5_fieldmd: 0x11f10
+  __TEXT.__swift5_fieldmd: 0x11f1c
   __TEXT.__swift5_proto: 0x2384
   __TEXT.__swift5_types: 0x13f8
   __TEXT.__swift5_assocty: 0x1620
-  __TEXT.__oslogstring: 0xede0
+  __TEXT.__oslogstring: 0xee70
   __TEXT.__swift5_builtin: 0xaa0
   __TEXT.__swift5_mpenum: 0x7a0
   __TEXT.__swift5_protos: 0x74

   __TEXT.__objc_methname: 0x179f
   __TEXT.__objc_methtype: 0x420
   __TEXT.__gcc_except_tab: 0x12c
-  __TEXT.__unwind_info: 0x10090
-  __TEXT.__eh_frame: 0x19548
+  __TEXT.__unwind_info: 0x10070
+  __TEXT.__eh_frame: 0x19578
   __DATA_CONST.__auth_got: 0x2228
   __DATA_CONST.__got: 0xc40
-  __DATA_CONST.__auth_ptr: 0x2fc8
-  __DATA_CONST.__const: 0x48708
+  __DATA_CONST.__auth_ptr: 0x2ff8
+  __DATA_CONST.__const: 0x48678
   __DATA_CONST.__cfstring: 0x20
-  __DATA_CONST.__objc_classlist: 0x1a0
+  __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x80
-  __DATA.__objc_const: 0x4340
+  __DATA.__objc_const: 0x42b0
   __DATA.__objc_selrefs: 0x888
-  __DATA.__objc_data: 0x980
-  __DATA.__data: 0x120e0
+  __DATA.__objc_data: 0x930
+  __DATA.__data: 0x12150
   __DATA.__bss: 0x45b30
-  __DATA.__common: 0xc80
+  __DATA.__common: 0xc70
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 26083
+  Functions: 26096
   Symbols:   457
   CStrings:  3001
 
Symbols:
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initEnumMetadataSinglePayloadWithLayoutString
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_instantiateLayoutString
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
+ _swift_cvw_singlePayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_singlePayloadEnumGeneric_getEnumTag
- _swift_allocateGenericValueMetadataWithLayoutString
- _swift_enumFn_getEnumTag
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_generic_instantiateLayoutString
- _swift_initEnumMetadataMultiPayloadWithLayoutString
- _swift_initEnumMetadataSinglePayloadWithLayoutString
- _swift_initStructMetadataWithLayoutString
- _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
- _swift_multiPayloadEnumGeneric_getEnumTag
- _swift_singlePayloadEnumGeneric_destructiveInjectEnumTag
- _swift_singlePayloadEnumGeneric_getEnumTag
CStrings:
+ "[%.*hhx-%{public}s] Ignoring invalid XAPPLEPUSHSERVICE response: %{sensitive}s"
+ "[%.*hhx] Created with environment %{public}s"
+ "[%.*hhx] Did clear wait-until-visible back-off."
+ "[%.*hhx] Did clear wait-until-visible back-off. Still backed-off for another %.*f seconds."
+ "[%.*hhx] Did mark %ld more mailboxes as sync complete."
+ "[%.*hhx] Did receive push registration info (%ld mailbox(es))."
+ "[%.*hhx] Did send action %s: did complete push registration (%ld mailbox(es))."
+ "[%.*hhx] Did send action %s: request push registration info."
+ "[%.*hhx] Received environment update: %{public}s"
+ "[%.*hhx] [{%.*hx}-%{sensitive,mask.mailbox}s] Did mark as sync complete."
- "[%.*hhx-%{public}s] %{sensitive,mask.mailbox}s ."
- "[%.*hhx-%{public}s] Did mark %ld more mailboxes as sync complete."
- "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] Did mark as sync complete."
- "[%.*hhx] Created with environment %s"
- "[%.*hhx] Received environment update: %s"
- "[%.*hhx] Received push registration info (%ld mailbox(es))."
- "[%.*hhx] Sending action %s: did complete push registration (%ld mailbox(es))."
- "[%.*hhx] Sending action %s: request push registration info."
- "_TtCV13IMAP2Behavior5State6Logger"
- "l"

```
