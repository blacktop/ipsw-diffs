## libsystem_sandbox.dylib

> `/usr/lib/system/libsystem_sandbox.dylib`

```diff

-2680.0.38.0.0
-  __TEXT.__text: 0x3544
+2680.0.42.0.0
+  __TEXT.__text: 0x3598
   __TEXT.__auth_stubs: 0x340
-  __TEXT.__const: 0x150
+  __TEXT.__const: 0x178
   __TEXT.__cstring: 0x741
   __TEXT.__unwind_info: 0x1b8
   __DATA_CONST.__got: 0x8

   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_platform.dylib
-  UUID: 9FCB2D99-9A5B-34DD-81E3-0EDEAD7A9F75
-  Functions: 128
-  Symbols:   236
+  UUID: 3FBC7AA6-682E-3E2F-ACD9-3BDCAE0B039F
+  Functions: 129
+  Symbols:   242
   CStrings:  66
 
Symbols:
+ _SANDBOX_STORAGE_CLASS_GROUP_ANY
+ _SANDBOX_STORAGE_CLASS_PROPERTY_ACCEPTS_USER_APPROVAL
+ _SANDBOX_STORAGE_CLASS_PROPERTY_READ_RESTRICTED
+ _SANDBOX_STORAGE_CLASS_PROPERTY_REPLACEMENT_RESTRICTED
+ _SANDBOX_STORAGE_CLASS_PROPERTY_WRITE_RESTRICTED
+ _sandbox_check_storage_class
Functions:
+ _sandbox_check_storage_class

```
