## Siri

> `/System/Library/DataClassMigrators/Siri.migrator/Siri`

```diff

-3520.86.6.0.0
-  __TEXT.__text: 0x300c
+3525.5.9.1.1
+  __TEXT.__text: 0x3180
   __TEXT.__auth_stubs: 0x350
-  __TEXT.__objc_stubs: 0x8c0
-  __TEXT.__objc_methlist: 0x128
+  __TEXT.__objc_stubs: 0x8e0
+  __TEXT.__objc_methlist: 0x134
   __TEXT.__const: 0x1c
-  __TEXT.__cstring: 0x61a
-  __TEXT.__oslogstring: 0x4df
+  __TEXT.__cstring: 0x69a
+  __TEXT.__oslogstring: 0x502
   __TEXT.__objc_classname: 0xd
-  __TEXT.__objc_methname: 0x6d4
+  __TEXT.__objc_methname: 0x711
   __TEXT.__objc_methtype: 0x20
-  __TEXT.__unwind_info: 0xa8
+  __TEXT.__unwind_info: 0xb0
   __DATA_CONST.__auth_got: 0x1b0
   __DATA_CONST.__got: 0xf0
   __DATA_CONST.__const: 0x10
-  __DATA_CONST.__cfstring: 0x4c0
+  __DATA_CONST.__cfstring: 0x4e0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x48
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x250
+  __DATA.__objc_selrefs: 0x258
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 25FB3D11-5F0E-378A-A182-7D86BD41AFEE
-  Functions: 27
+  UUID: 208A81CF-1330-3609-9077-81B21210C2CA
+  Functions: 28
   Symbols:   95
-  CStrings:  202
+  CStrings:  207
 
CStrings:
+ "%s No history to remove. Skipping."
+ "-[SiriMigrator _performRemoveAnnounceNotificationsThreadCancellationHistory]"
+ "Announce Notifications Thread Cancellation History"
+ "_performRemoveAnnounceNotificationsThreadCancellationHistory"

```
