## remindd

> `/usr/libexec/remindd`

```diff

-3900.0.0.0.0
-  __TEXT.__text: 0x7728a4
-  __TEXT.__auth_stubs: 0x8450
+3900.1.0.0.0
+  __TEXT.__text: 0x774bc0
+  __TEXT.__auth_stubs: 0x8470
   __TEXT.__objc_stubs: 0x10080
-  __TEXT.__objc_methlist: 0xa870
-  __TEXT.__const: 0x27d88
+  __TEXT.__objc_methlist: 0xa8a0
+  __TEXT.__const: 0x27eb8
   __TEXT.__objc_methname: 0x23207
   __TEXT.__objc_classname: 0x159f
   __TEXT.__objc_methtype: 0x3882
   __TEXT.__gcc_except_tab: 0x26cc
-  __TEXT.__cstring: 0x2061a
-  __TEXT.__oslogstring: 0x5dad0
+  __TEXT.__cstring: 0x2067a
+  __TEXT.__oslogstring: 0x5dc90
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_typeref: 0x13c76
-  __TEXT.__swift5_fieldmd: 0xa338
-  __TEXT.__constg_swiftt: 0xc96c
+  __TEXT.__swift5_typeref: 0x13ca6
+  __TEXT.__swift5_fieldmd: 0xa354
+  __TEXT.__constg_swiftt: 0xc9a8
   __TEXT.__swift5_builtin: 0x398
-  __TEXT.__swift5_reflstr: 0xbd85
+  __TEXT.__swift5_reflstr: 0xbdb5
   __TEXT.__swift5_assocty: 0x1e88
-  __TEXT.__swift5_capture: 0x5ff4
+  __TEXT.__swift5_capture: 0x601c
   __TEXT.__swift5_protos: 0x2c8
   __TEXT.__swift5_proto: 0x1854
-  __TEXT.__swift5_types: 0xad8
+  __TEXT.__swift5_types: 0xadc
   __TEXT.__swift_as_entry: 0x168
   __TEXT.__swift_as_ret: 0x1cc
   __TEXT.__swift5_mpenum: 0xc4
-  __TEXT.__unwind_info: 0x10358
-  __TEXT.__eh_frame: 0x208ec
-  __DATA_CONST.__auth_got: 0x4238
-  __DATA_CONST.__got: 0x32d8
-  __DATA_CONST.__auth_ptr: 0x26b8
-  __DATA_CONST.__const: 0x253d0
+  __TEXT.__unwind_info: 0x10398
+  __TEXT.__eh_frame: 0x2098c
+  __DATA_CONST.__auth_got: 0x4248
+  __DATA_CONST.__got: 0x32d0
+  __DATA_CONST.__auth_ptr: 0x26c8
+  __DATA_CONST.__const: 0x25448
   __DATA_CONST.__cfstring: 0x50e0
-  __DATA_CONST.__objc_classlist: 0xbd8
+  __DATA_CONST.__objc_classlist: 0xbe0
   __DATA_CONST.__objc_catlist: 0x110
   __DATA_CONST.__objc_catlist2: 0x10
   __DATA_CONST.__objc_protolist: 0x520

   __DATA_CONST.__objc_arrayobj: 0x360
   __DATA_CONST.__objc_dictobj: 0x140
   __DATA_CONST.__objc_doubleobj: 0x30
-  __DATA.__objc_const: 0x1d1d0
+  __DATA.__objc_const: 0x1d248
   __DATA.__objc_selrefs: 0x7aa8
   __DATA.__objc_ivar: 0x480
-  __DATA.__objc_data: 0x8388
-  __DATA.__data: 0x1e2d0
+  __DATA.__objc_data: 0x8448
+  __DATA.__data: 0x1e2f0
   __DATA.__objc_stublist: 0x38
-  __DATA.__bss: 0x227c0
+  __DATA.__bss: 0x227e0
   __DATA.__common: 0x9e8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BB7913D4-F243-38A2-9CFE-98F432761B22
-  Functions: 22327
-  Symbols:   4074
-  CStrings:  12718
+  UUID: 63A669CB-F029-3079-882D-490FC20D8E82
+  Functions: 22356
+  Symbols:   4075
+  CStrings:  12721
 
Symbols:
+ _RDStoreControllerUpdateReminderIsUrgentStateEnabledForCurrentUserMigratorAuthor
CStrings:
+ "%{public}s#mergeData(from record: CKRecord, accountID:): Failed to recompute '\\REMCDReminder.isUrgentStateEnabledForCurrentUser' after updating '\\REMCDAccount.personIDSalt'. {account.objectID: %{public}s, error: %{public}s}"
+ "%{public}s#mergeData(from record: CKRecord, accountID:): Recomputed '\\REMCDReminder.isUrgentStateEnabledForCurrentUser' after updating '\\REMCDAccount.personIDSalt'. {account.objectID: %{public}s, updateCount: %{public}ld}"
+ "_TtC7remindd74RDStoreControllerMigrator_UpdateReminderIsUrgentStateEnabledForCurrentUser"

```
