## DeviceManagement

> `/System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement`

```diff

-221.2.7.0.0
-  __TEXT.__text: 0x3673c
-  __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_methlist: 0x6dd0
+221.4.6.0.0
+  __TEXT.__text: 0x37f60
+  __TEXT.__auth_stubs: 0x640
+  __TEXT.__objc_methlist: 0x7334
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x508a
-  __TEXT.__oslogstring: 0xe06
+  __TEXT.__cstring: 0x509c
+  __TEXT.__oslogstring: 0xebc
   __TEXT.__ustring: 0xb64
-  __TEXT.__gcc_except_tab: 0x2cc
-  __TEXT.__unwind_info: 0xe68
-  __TEXT.__objc_classname: 0x173b
-  __TEXT.__objc_methname: 0x9b41
-  __TEXT.__objc_methtype: 0xade
-  __TEXT.__objc_stubs: 0x4c60
-  __DATA_CONST.__got: 0x358
-  __DATA_CONST.__const: 0xe18
-  __DATA_CONST.__objc_classlist: 0x600
+  __TEXT.__gcc_except_tab: 0x2f8
+  __TEXT.__unwind_info: 0xf30
+  __TEXT.__objc_classname: 0x178e
+  __TEXT.__objc_methname: 0x9cb9
+  __TEXT.__objc_methtype: 0xb24
+  __TEXT.__objc_stubs: 0x4d00
+  __DATA_CONST.__got: 0x368
+  __DATA_CONST.__const: 0xe90
+  __DATA_CONST.__objc_classlist: 0x618
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1cd0
+  __DATA_CONST.__objc_selrefs: 0x1da0
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x4b8
-  __DATA_CONST.__objc_arraydata: 0x680
-  __AUTH_CONST.__auth_got: 0x318
-  __AUTH_CONST.__const: 0x480
-  __AUTH_CONST.__cfstring: 0x73c0
-  __AUTH_CONST.__objc_const: 0x10320
-  __AUTH_CONST.__objc_intobj: 0x14b8
-  __AUTH_CONST.__objc_arrayobj: 0x858
-  __AUTH.__objc_data: 0x3480
-  __DATA.__objc_ivar: 0x89c
+  __DATA_CONST.__objc_superrefs: 0x4c8
+  __DATA_CONST.__objc_arraydata: 0x6a0
+  __AUTH_CONST.__auth_got: 0x330
+  __AUTH_CONST.__const: 0x4a0
+  __AUTH_CONST.__cfstring: 0x7400
+  __AUTH_CONST.__objc_const: 0x102c8
+  __AUTH_CONST.__objc_intobj: 0x1518
+  __AUTH_CONST.__objc_arrayobj: 0x888
+  __AUTH.__objc_data: 0x3570
+  __DATA.__objc_ivar: 0x8d4
   __DATA.__data: 0x430
-  __DATA.__bss: 0x118
+  __DATA.__bss: 0x128
   __DATA_DIRTY.__objc_data: 0x780
   __DATA_DIRTY.__bss: 0xe0
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2253
-  Symbols:   3035
-  CStrings:  3065
+  Functions: 2341
+  Symbols:   3154
+  CStrings:  3089
 
Symbols:
+ _OBJC_CLASS_$_DMFFetchAppInfoRequest
+ _OBJC_CLASS_$_DMFFetchAppInfoResultObject
+ _OBJC_CLASS_$_DMFUpdateAppAttributesRequest
+ _OBJC_METACLASS_$_DMFFetchAppInfoRequest
+ _OBJC_METACLASS_$_DMFFetchAppInfoResultObject
+ _OBJC_METACLASS_$_DMFUpdateAppAttributesRequest
+ ___NSDictionary0__struct
+ _objc_getProperty
+ _objc_retainAutoreleasedReturnValue
+ _objc_setProperty_atomic_copy
CStrings:
+ "\x11\x1c"
+ "\x1b"
+ "Attributes"
+ "DMFFetchAppInfoRequest"
+ "DMFFetchAppInfoResultObject"
+ "DMFUpdateAppAttributesRequest"
+ "Failed to create an operation for request: \"%{public}@\": %{public}@"
+ "Failed to filter %lu identifiers with error: %{public}@"
+ "Successfully filtered %lu identifiers. Result: %@{public}"
+ "T@\"NSDictionary\",C,V_policiesByBundleIdentifier"
+ "T@\"NSDictionary\",R,C,N,V_managedApps"
+ "TB,N,V_ignoreNilConfiguration"
+ "_ignoreNilConfiguration"
+ "_managedApps"
+ "addAttributes:forApp:"
+ "allEffectivePolicyTypes"
+ "filterForExpiredBudgetIdentifiers:completionHandler:"
+ "filterForExpiredBudgetIdentifiers:shouldBeSynchronous:replyHandler:"
+ "filterForExpiredBudgetIdentifiers:withError:"
+ "ignoreNilConfiguration"
+ "managedApps"
+ "setIgnoreNilConfiguration:"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "v36@0:8@\"NSArray\"16B24@?<v@?@\"NSArray\"@\"NSError\">28"
+ "v36@0:8@16B24@?28"
- "\x01\x1c"
- "T@\"NSDictionary\",C,N,V_policiesByBundleIdentifier"
- "connection %@ did not return an operation for request: %@"

```
