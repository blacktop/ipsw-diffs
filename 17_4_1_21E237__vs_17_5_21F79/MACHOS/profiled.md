## profiled

> `/usr/libexec/profiled`

```diff

-2288.0.1.0.0
-  __TEXT.__text: 0x99b40
+2295.0.0.0.0
+  __TEXT.__text: 0x9a030
   __TEXT.__auth_stubs: 0x20f0
-  __TEXT.__objc_stubs: 0xf520
-  __TEXT.__objc_methlist: 0x4bb0
+  __TEXT.__objc_stubs: 0xf5a0
+  __TEXT.__objc_methlist: 0x4bb8
   __TEXT.__gcc_except_tab: 0x128c
-  __TEXT.__oslogstring: 0xc19b
-  __TEXT.__cstring: 0x8aab
+  __TEXT.__oslogstring: 0xc2a3
+  __TEXT.__cstring: 0x8ac3
   __TEXT.__const: 0x68
-  __TEXT.__objc_methname: 0x12ea6
+  __TEXT.__objc_methname: 0x12f1c
   __TEXT.__objc_classname: 0xb36
-  __TEXT.__objc_methtype: 0x1fb6
-  __TEXT.__unwind_info: 0x15d4
+  __TEXT.__objc_methtype: 0x1f75
+  __TEXT.__unwind_info: 0x15d0
   __DATA_CONST.__auth_got: 0x1088
-  __DATA_CONST.__got: 0x15a0
+  __DATA_CONST.__got: 0x15c0
   __DATA_CONST.__const: 0x1b00
-  __DATA_CONST.__cfstring: 0x8420
+  __DATA_CONST.__cfstring: 0x8440
   __DATA_CONST.__objc_classlist: 0x2c8
   __DATA_CONST.__objc_catlist: 0x1e8
   __DATA_CONST.__objc_protolist: 0x68

   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0x71b0
-  __DATA.__objc_selrefs: 0x41c8
+  __DATA.__objc_selrefs: 0x41e8
   __DATA.__objc_ivar: 0x1c0
   __DATA.__objc_data: 0x1bd0
   __DATA.__data: 0x4ea

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1901
-  Symbols:   1436
-  CStrings:  4801
+  Functions: 1902
+  Symbols:   1440
+  CStrings:  4809
 
Symbols:
+ _ACAccountTypeIdentifierAol
+ _ACAccountTypeIdentifierIMAPMail
+ _ACAccountTypeIdentifierYahoo
+ _MCFeatureNotificationRestrictedApps
CStrings:
+ "CLOUD_CONFIG_SAVE_ERROR"
+ "Could not store cloud configuration."
+ "Could not store set aside details."
+ "Failed to remove personaIdentifer for mail account: %@, error: %{public}@"
+ "Failed to store profile data with error: %{public}@"
+ "Failed to store set aside profile data with error: %{public}@"
+ "Removing personaIdentifer for mail account: %@"
+ "_removePersonaIDForMailAccountWithPersistentResourceID:"
+ "accountsWithAccountTypeIdentifiers:error:"
+ "personaIdentifier"
+ "saveVerifiedAccount:error:"
+ "storeProfileData:completion:"
- "Unknown profile storage purpose. Ignoring."
- "storeProfileData:configurationSource:purpose:completion:"
- "v40@0:8@\"NSData\"16i24i28@?<v@?@\"NSError\">32"
- "v40@0:8@16i24i28@?32"

```
