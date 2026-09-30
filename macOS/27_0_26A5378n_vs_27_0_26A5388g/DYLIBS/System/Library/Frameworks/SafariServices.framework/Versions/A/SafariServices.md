## SafariServices

> `/System/Library/Frameworks/SafariServices.framework/Versions/A/SafariServices`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__got`
- `__DATA_DIRTY.__objc_data`

```diff

-625.1.22.11.4
-  __TEXT.__text: 0x17c84
-  __TEXT.__objc_methlist: 0x157c
-  __TEXT.__gcc_except_tab: 0x1d70
-  __TEXT.__cstring: 0x19b1
+625.1.24.11.2
+  __TEXT.__text: 0x18560
+  __TEXT.__objc_methlist: 0x1604
+  __TEXT.__gcc_except_tab: 0x1d90
+  __TEXT.__cstring: 0x1a95
   __TEXT.__const: 0xa0
-  __TEXT.__oslogstring: 0xc60
-  __TEXT.__unwind_info: 0xc50
+  __TEXT.__oslogstring: 0xca7
+  __TEXT.__unwind_info: 0xc90
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x138
-  __DATA_CONST.__objc_classlist: 0xf8
+  __DATA_CONST.__const: 0x140
+  __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x78
+  __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xec0
-  __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x78
+  __DATA_CONST.__objc_selrefs: 0xee8
+  __DATA_CONST.__objc_protorefs: 0x30
+  __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__got: 0x208
-  __AUTH_CONST.__const: 0xdb0
-  __AUTH_CONST.__cfstring: 0x900
-  __AUTH_CONST.__objc_const: 0x2330
+  __AUTH_CONST.__const: 0xe40
+  __AUTH_CONST.__cfstring: 0x9a0
+  __AUTH_CONST.__objc_const: 0x2518
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x870
-  __DATA.__objc_ivar: 0xa4
-  __DATA.__data: 0x5b0
+  __AUTH.__objc_data: 0x910
+  __DATA.__objc_ivar: 0xac
+  __DATA.__data: 0x610
   __DATA.__bss: 0x110
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x140

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 660
-  Symbols:   1601
-  CStrings:  227
+  Functions: 675
+  Symbols:   1647
+  CStrings:  235
 
Symbols:
+ +[SFSafariSettings _currentProcessIsWebExtension]
+ +[SFSafariSettings checkAutoFillUserNamesAndPasswordsEnabledWithCompletionHandler:]
+ -[SFSafariSettingsHelperProxy .cxx_destruct]
+ -[SFSafariSettingsHelperProxy _connectionCreatingIfNecessary]
+ -[SFSafariSettingsHelperProxy _createConnection]
+ -[SFSafariSettingsHelperProxy dealloc]
+ -[SFSafariSettingsHelperProxy getSafariPasswordAutoFillSettingWithCompletionHandler:]
+ -[SFSafariSettingsHelperProxy init]
+ OBJC_IVAR_$_SFSafariSettingsHelperProxy._connection
+ OBJC_IVAR_$_SFSafariSettingsHelperProxy._connectionLock
+ _OBJC_CLASS_$_SFSafariSettings
+ _OBJC_CLASS_$_SFSafariSettingsHelperProxy
+ _OBJC_METACLASS_$_SFSafariSettings
+ _OBJC_METACLASS_$_SFSafariSettingsHelperProxy
+ _SFSafariSettingsErrorDomain
+ __83+[SFSafariSettings checkAutoFillUserNamesAndPasswordsEnabledWithCompletionHandler:]_block_invoke
+ __85-[SFSafariSettingsHelperProxy getSafariPasswordAutoFillSettingWithCompletionHandler:]_block_invoke
+ __OBJC_$_CLASS_METHODS_SFSafariSettings
+ __OBJC_$_INSTANCE_METHODS_SFSafariSettingsHelperProxy
+ __OBJC_$_INSTANCE_VARIABLES_SFSafariSettingsHelperProxy
+ __OBJC_$_PROP_LIST_SFSafariSettingsHelperProxy
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ASCSafariSettingsHelperProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ASCSafariSettingsHelperProtocol
+ __OBJC_$_PROTOCOL_REFS_ASCSafariSettingsHelperProtocol
+ __OBJC_CLASS_PROTOCOLS_$_SFSafariSettingsHelperProxy
+ __OBJC_CLASS_RO_$_SFSafariSettings
+ __OBJC_CLASS_RO_$_SFSafariSettingsHelperProxy
+ __OBJC_LABEL_PROTOCOL_$_ASCSafariSettingsHelperProtocol
+ __OBJC_METACLASS_RO_$_SFSafariSettings
+ __OBJC_METACLASS_RO_$_SFSafariSettingsHelperProxy
+ __OBJC_PROTOCOL_$_ASCSafariSettingsHelperProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_ASCSafariSettingsHelperProtocol
+ ___48-[SFSafariSettingsHelperProxy _createConnection]_block_invoke
+ ___83+[SFSafariSettings checkAutoFillUserNamesAndPasswordsEnabledWithCompletionHandler:]_block_invoke
+ ___85-[SFSafariSettingsHelperProxy getSafariPasswordAutoFillSettingWithCompletionHandler:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e17_v16?0"NSError"8l
+ ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12l
+ ___block_descriptor_48_e8_32s40w_e5_v8?0l
+ ___copy_helper_block_e8_32s40w
+ ___destroy_helper_block_e8_32s40w
+ _objc_msgSend$_connectionCreatingIfNecessary
+ _objc_msgSend$_createConnection
+ _objc_msgSend$_currentProcessIsWebExtension
+ _objc_msgSend$getSafariPasswordAutoFillSettingWithCompletionHandler:
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
CStrings:
+ "Error returned from proxy: %{private}@"
+ "NSExtension"
+ "NSExtensionPointIdentifier"
+ "Remote proxy error: %{private}@"
+ "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent"
+ "com.apple.AuthenticationServicesCore.AuthorizationError"
+ "com.apple.SafariServices.SFSafariSettingsError"
+ "v20@?0B8@\"NSError\"12"
```
