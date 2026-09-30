## MergeBuddyProvisioningResponse

> `/System/Library/DataClassMigrators/MergeBuddyProvisioningResponse.migrator/MergeBuddyProvisioningResponse`

```diff

-1007.477.0.0.0
+1025.0.0.0.0
   __TEXT.__text: 0x2d54
   __TEXT.__auth_stubs: 0x2e0
   __TEXT.__objc_stubs: 0x9c0

   __TEXT.__const: 0x38
   __TEXT.__gcc_except_tab: 0x50
   __TEXT.__cstring: 0x3bc
-  __TEXT.__oslogstring: 0x7aa
+  __TEXT.__oslogstring: 0x7b0
   __TEXT.__objc_classname: 0x1f
   __TEXT.__objc_methname: 0x7ee
   __TEXT.__objc_methtype: 0x72

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ED88BD18-8138-3E58-8300-45079E589C92
+  UUID: 3B9378E6-223B-3442-88F5-B9938DDF3C71
   Functions: 51
   Symbols:   81
   CStrings:  163
CStrings:
+ "No AuthKit account to remove device-specific credentials for altDSID: %{mask}@"
- "No AuthKit account to remove device-specific credentials for altDSID: %@"

```
