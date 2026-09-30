## installd

> `/usr/libexec/installd`

```diff

-1513.120.6.0.0
-  __TEXT.__text: 0x60dec
+1513.120.7.0.0
+  __TEXT.__text: 0x60f9c
   __TEXT.__auth_stubs: 0xf80
   __TEXT.__objc_stubs: 0x8220
   __TEXT.__objc_methlist: 0x335c
   __TEXT.__const: 0x120
-  __TEXT.__cstring: 0x166dc
+  __TEXT.__cstring: 0x169d2
   __TEXT.__objc_classname: 0x613
   __TEXT.__objc_methtype: 0x1fe2
   __TEXT.__objc_methname: 0xbfd7

   __DATA_CONST.__got: 0x368
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x1248
-  __DATA_CONST.__cfstring: 0x9c60
+  __DATA_CONST.__cfstring: 0x9ce0
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xc0

   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 96333FB4-1148-3EE9-BA59-C05B166C4DA7
-  Functions: 1290
+  UUID: E28314C2-BDC4-3321-B046-31A17F97C40A
+  Functions: 1291
   Symbols:   371
-  CStrings:  4885
+  CStrings:  4893
 
Functions:
~ sub_100049850 : 1352 -> 1768
+ sub_100054be4
CStrings:
+ "The app being installed, \"%@\", has an accessory data transport app extension at \"%@\" but that extension does not have the required entitlement and value for that type of extension, \"%@\" = TRUE (boolean). Accessory data transport app extensions must have this entitlement and value."
+ "The app being installed, \"%@\", has an app extension at \"%@\" that is not an accessory data transport extension but has that extension type's corresponding entitlement \"%@\". Only accessory data transport app extensions are allowed to have this entitlement."
+ "The app being installed, \"%@\", has the entitlement \"%@\" which is not allowed on an app. Only accessory data transport app extensions are allowed to have this entitlement."
+ "com.apple.developer.accessory-transport-extension"

```
