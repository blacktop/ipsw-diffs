## Accounts

> `/System/Library/Frameworks/Accounts.framework/Accounts`

```diff

-1022.0.0.0.0
-  __TEXT.__text: 0x5ca60
+1023.0.0.0.0
+  __TEXT.__text: 0x5ca78
   __TEXT.__auth_stubs: 0xc90
   __TEXT.__objc_methlist: 0x42dc
   __TEXT.__const: 0xc8
-  __TEXT.__gcc_except_tab: 0x3ed0
+  __TEXT.__gcc_except_tab: 0x3ee0
   __TEXT.__cstring: 0x3d20
-  __TEXT.__oslogstring: 0x52b5
+  __TEXT.__oslogstring: 0x52c8
   __TEXT.__unwind_info: 0x1a78
   __TEXT.__objc_classname: 0x599
   __TEXT.__objc_methname: 0x8997

   __DATA.__bss: 0x109
   __DATA_DIRTY.__objc_data: 0x730
   __DATA_DIRTY.__data: 0x4
-  __DATA_DIRTY.__bss: 0xd0
+  __DATA_DIRTY.__bss: 0xd8
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 292C10A9-C685-3A52-BFF4-26E4244AF132
-  Functions: 1959
-  Symbols:   6757
+  UUID: F9424F75-810A-3119-809B-2215D0288CC6
+  Functions: 1958
+  Symbols:   6755
   CStrings:  3438
 
Symbols:
- -[ACAccount initWithManagedAccount:].cold.1
Functions:
~ -[ACAccount initWithManagedAccount:] : 1644 -> 1748
- -[ACAccount initWithManagedAccount:].cold.1
~ -[ACAccount setSecCertificates:].cold.1 : 124 -> 112
~ -[ACAccount correctPersonaScopedForAccount].cold.1 : 128 -> 140
~ -[ACAccount correctPersonaScopedForAccount].cold.2 : 128 -> 140
CStrings:
+ "\"Unexpecteed nil value for property %@ or key %@\""
- "\"Unexpecteed nil value for %@\""

```
