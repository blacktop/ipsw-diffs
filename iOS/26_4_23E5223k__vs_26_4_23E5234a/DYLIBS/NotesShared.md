## NotesShared

> `/System/Library/PrivateFrameworks/NotesShared.framework/NotesShared`

```diff

-2952.100.24.102.1
-  __TEXT.__text: 0x363c98
+2952.102.3.0.0
+  __TEXT.__text: 0x363de4
   __TEXT.__auth_stubs: 0x5230
   __TEXT.__delay_stubs: 0x240
   __TEXT.__delay_helper: 0x830
-  __TEXT.__objc_methlist: 0x17e6c
+  __TEXT.__objc_methlist: 0x17e8c
   __TEXT.__const: 0xdcf8
   __TEXT.__cstring: 0x18e41
   __TEXT.__oslogstring: 0x1be18

   __TEXT.__swift_as_entry: 0x19c
   __TEXT.__swift_as_ret: 0x1c8
   __TEXT.__swift5_mpenum: 0x74
-  __TEXT.__unwind_info: 0xf550
+  __TEXT.__unwind_info: 0xf568
   __TEXT.__eh_frame: 0x8ce8
   __TEXT.__objc_classname: 0x2ada
-  __TEXT.__objc_methname: 0x37a7f
+  __TEXT.__objc_methname: 0x37aaf
   __TEXT.__objc_methtype: 0x516f
   __TEXT.__objc_stubs: 0x28780
   __DATA_CONST.__got: 0x2130

   __DATA_CONST.__objc_catlist: 0x138
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc980
+  __DATA_CONST.__objc_selrefs: 0xc988
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x6b8
   __DATA_CONST.__objc_arraydata: 0x1e8
   __AUTH_CONST.__auth_got: 0x2978
-  __AUTH_CONST.__const: 0xd7b0
-  __AUTH_CONST.__cfstring: 0xf460
-  __AUTH_CONST.__objc_const: 0x21ce0
+  __AUTH_CONST.__const: 0xd7d0
+  __AUTH_CONST.__cfstring: 0xf480
+  __AUTH_CONST.__objc_const: 0x21d10
   __AUTH_CONST.__objc_intobj: 0x438
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x2f40
   __AUTH.__data: 0x14b0
-  __DATA.__objc_ivar: 0xd54
+  __DATA.__objc_ivar: 0xd58
   __DATA.__data: 0x4aa4
   __DATA.__objc_stublist: 0x20
-  __DATA.__bss: 0x10920
+  __DATA.__bss: 0x10930
   __DATA.__common: 0x180
   __DATA_DIRTY.__objc_data: 0x46a8
   __DATA_DIRTY.__data: 0x1bb8

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7FAA541D-A19F-3C8B-9773-317A6B80FEC0
-  Functions: 18396
-  Symbols:   38885
-  CStrings:  16501
+  UUID: ADA777DD-3B08-3ED6-839C-C24EF986062B
+  Functions: 18401
+  Symbols:   38900
+  CStrings:  16506
 
Symbols:
+ +[ICNoteContext isDaemonProcess]
+ +[ICNoteContext isDaemonProcess].cold.1
+ -[ICCloudContext isDaemonProcess]
+ -[ICCloudContext setIsDaemonProcess:]
+ GCC_except_table573
+ GCC_except_table576
+ GCC_except_table577
+ GCC_except_table614
+ GCC_except_table615
+ GCC_except_table645
+ GCC_except_table664
+ _OBJC_IVAR_$_ICCloudContext._isDaemonProcess
+ ___31-[ICNoteContext updateAccounts]_block_invoke.192
+ ___31-[ICNoteContext updateAccounts]_block_invoke_2.195
+ ___32+[ICNoteContext isDaemonProcess]_block_invoke
+ ___36-[ICNoteContext persistentContainer]_block_invoke.267
+ ___36-[ICNoteContext persistentContainer]_block_invoke_2.269
+ ___40-[ICNoteContext setupTrashDeletionTimer]_block_invoke.146
+ ___50-[ICNoteContext cleanupAdditionalPersistentStores]_block_invoke.284
+ ___50-[ICNoteContext cleanupAdditionalPersistentStores]_block_invoke.284.cold.1
+ ___50-[ICNoteContext cleanupAdditionalPersistentStores]_block_invoke.284.cold.2
+ ___63-[ICNote(AttachmentManagement) addMediaToAttachment:withBlock:]_block_invoke.1185
+ ___63-[ICNote(AttachmentManagement) addMediaToAttachment:withBlock:]_block_invoke.1185.cold.1
+ ___63-[ICNote(AttachmentManagement) addMediaToAttachment:withBlock:]_block_invoke.1185.cold.2
+ ___63-[ICNote(AttachmentManagement) addMediaToAttachment:withBlock:]_block_invoke.1186
+ ___63-[ICNote(AttachmentManagement) addMediaToAttachment:withBlock:]_block_invoke.1187
+ ___63-[ICNote(AttachmentManagement) addMediaToAttachment:withBlock:]_block_invoke.1187.cold.1
+ ___92-[ICNoteContext createAdditionalPersistentStoresWithAccountIdentifiers:persistentContainer:]_block_invoke.280
+ ___92-[ICNoteContext createAdditionalPersistentStoresWithAccountIdentifiers:persistentContainer:]_block_invoke.280.cold.1
+ ___92-[ICNoteContext createAdditionalPersistentStoresWithAccountIdentifiers:persistentContainer:]_block_invoke.280.cold.2
+ ___block_literal_global.1054
+ ___block_literal_global.109
+ ___block_literal_global.1153
+ ___block_literal_global.1166
+ ___block_literal_global.1182
+ ___block_literal_global.141
+ ___block_literal_global.162
+ ___block_literal_global.194
+ ___block_literal_global.198
+ ___block_literal_global.275
+ ___block_literal_global.282
+ ___block_literal_global.284
+ ___block_literal_global.287
+ ___block_literal_global.292
+ ___block_literal_global.345
+ ___block_literal_global.356
+ ___block_literal_global.359
+ ___block_literal_global.490
+ ___block_literal_global.587
+ ___block_literal_global.76
+ ___block_literal_global.78
+ __isDaemonProcess
+ _isDaemonProcess.onceToken
+ _sharedContextInitInProgress
- GCC_except_table571
- GCC_except_table574
- GCC_except_table575
- GCC_except_table611
- GCC_except_table612
- GCC_except_table643
- GCC_except_table662
- ___31-[ICNoteContext updateAccounts]_block_invoke.186
- ___31-[ICNoteContext updateAccounts]_block_invoke_2.189
- ___36-[ICNoteContext persistentContainer]_block_invoke.261
- ___36-[ICNoteContext persistentContainer]_block_invoke_2.263
- ___40-[ICNoteContext setupTrashDeletionTimer]_block_invoke.140
- ___50-[ICNoteContext cleanupAdditionalPersistentStores]_block_invoke.278
- ___50-[ICNoteContext cleanupAdditionalPersistentStores]_block_invoke.278.cold.1
- ___50-[ICNoteContext cleanupAdditionalPersistentStores]_block_invoke.278.cold.2
- ___63-[ICNote(AttachmentManagement) addMediaToAttachment:withBlock:]_block_invoke.1181
- ___63-[ICNote(AttachmentManagement) addMediaToAttachment:withBlock:]_block_invoke.1181.cold.1
- ___63-[ICNote(AttachmentManagement) addMediaToAttachment:withBlock:]_block_invoke.1181.cold.2
- ___63-[ICNote(AttachmentManagement) addMediaToAttachment:withBlock:]_block_invoke.1182
- ___63-[ICNote(AttachmentManagement) addMediaToAttachment:withBlock:]_block_invoke.1183
- ___63-[ICNote(AttachmentManagement) addMediaToAttachment:withBlock:]_block_invoke.1183.cold.1
- ___92-[ICNoteContext createAdditionalPersistentStoresWithAccountIdentifiers:persistentContainer:]_block_invoke.274
- ___92-[ICNoteContext createAdditionalPersistentStoresWithAccountIdentifiers:persistentContainer:]_block_invoke.274.cold.1
- ___92-[ICNoteContext createAdditionalPersistentStoresWithAccountIdentifiers:persistentContainer:]_block_invoke.274.cold.2
- ___block_literal_global.103
- ___block_literal_global.1050
- ___block_literal_global.1149
- ___block_literal_global.1162
- ___block_literal_global.1178
- ___block_literal_global.135
- ___block_literal_global.156
- ___block_literal_global.188
- ___block_literal_global.268
- ___block_literal_global.271
- ___block_literal_global.280
- ___block_literal_global.281
- ___block_literal_global.288
- ___block_literal_global.341
- ___block_literal_global.352
- ___block_literal_global.355
- ___block_literal_global.486
- ___block_literal_global.583
- ___block_literal_global.72
CStrings:
+ "Note deleted"
+ "TB,N,V_isDaemonProcess"
+ "_isDaemonProcess"
+ "setIsDaemonProcess:"

```
