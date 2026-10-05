## CallKit

> `/System/Library/Frameworks/CallKit.framework/CallKit`

```diff

-1406.200.62.0.0
-  __TEXT.__text: 0x659d0
+1406.200.81.0.0
+  __TEXT.__text: 0x665d0
   __TEXT.__objc_methlist: 0x9324
   __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x641a
-  __TEXT.__oslogstring: 0x3d16
-  __TEXT.__gcc_except_tab: 0x6f8
-  __TEXT.__unwind_info: 0x2938
+  __TEXT.__cstring: 0x6557
+  __TEXT.__oslogstring: 0x3e91
+  __TEXT.__gcc_except_tab: 0x784
+  __TEXT.__unwind_info: 0x2968
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xde0
+  __DATA_CONST.__const: 0xe08
   __DATA_CONST.__objc_classlist: 0x410
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x1f0

   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__got: 0x4f0
   __AUTH_CONST.__const: 0x560
-  __AUTH_CONST.__cfstring: 0x43a0
+  __AUTH_CONST.__cfstring: 0x4440
   __AUTH_CONST.__objc_const: 0xf138
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x48

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3259
-  Symbols:   5469
-  CStrings:  1014
+  Functions: 3269
+  Symbols:   5473
+  CStrings:  1031
 
Symbols:
+ GCC_except_table97
+ _OUTLINED_FUNCTION_5
+ ___94-[CXCallDirectoryStore migrateAllDataFromExtensionWithBundleID:toExtensionWithBundleID:error:]_block_invoke
+ ___block_descriptor_72_e8_32s40s48s56r64r_e20_B24?0?<B?^>8^16ls32l8r56l8r64l8s40l8s48l8
CStrings:
+ "DELETE FROM Extension WHERE bundle_id = ?"
+ "Deleting old extension"
+ "Executing migration"
+ "Failed to delete old extension: %@"
+ "Failed to update blocking entries: %@"
+ "Failed to update identification entries: %@"
+ "Failed to update new extension state: %@"
+ "Getting new extension's unique id"
+ "Getting old extension's data"
+ "New extension's unique id not found"
+ "Old extension not found"
+ "SELECT id FROM Extension WHERE bundle_id = ?"
+ "SELECT id, priority, state FROM Extension WHERE bundle_id = ?"
+ "UPDATE Extension SET priority = ?, state = ? WHERE bundle_id = ?"
+ "UPDATE PhoneNumberBlockingEntry SET extension_id = ? WHERE extension_id = ?"
+ "UPDATE PhoneNumberIdentificationEntry SET extension_id = ? WHERE extension_id = ?"
+ "Updating blocking entries"
+ "Updating identification entries"
+ "Updating new extension state"
- "Executing application migration"
- "UPDATE Extension SET bundle_id = ? WHERE bundle_id = ?"
```
