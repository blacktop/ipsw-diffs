## InstallCoordination

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination`

```diff

-775.0.0.0.0
-  __TEXT.__text: 0x6a140
+781.0.0.0.1
+  __TEXT.__text: 0x6b988
   __TEXT.__auth_stubs: 0xb60
-  __TEXT.__objc_methlist: 0x4158
+  __TEXT.__objc_methlist: 0x4238
   __TEXT.__const: 0x110
-  __TEXT.__cstring: 0xe97e
-  __TEXT.__oslogstring: 0x7ab0
-  __TEXT.__gcc_except_tab: 0x1dbc
+  __TEXT.__cstring: 0xed03
+  __TEXT.__oslogstring: 0x7c82
+  __TEXT.__gcc_except_tab: 0x1e40
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x17e8
-  __TEXT.__objc_classname: 0x8ae
-  __TEXT.__objc_methname: 0xada5
-  __TEXT.__objc_methtype: 0x23eb
-  __TEXT.__objc_stubs: 0x60c0
-  __DATA_CONST.__got: 0x3f0
-  __DATA_CONST.__const: 0x1bc0
-  __DATA_CONST.__objc_classlist: 0x198
+  __TEXT.__unwind_info: 0x1850
+  __TEXT.__objc_classname: 0x8df
+  __TEXT.__objc_methname: 0xafca
+  __TEXT.__objc_methtype: 0x2416
+  __TEXT.__objc_stubs: 0x6180
+  __DATA_CONST.__got: 0x3f8
+  __DATA_CONST.__const: 0x1be8
+  __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x20a0
+  __DATA_CONST.__objc_selrefs: 0x2118
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x130
+  __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_arraydata: 0x108
   __AUTH_CONST.__auth_got: 0x5c0
   __AUTH_CONST.__const: 0x360
-  __AUTH_CONST.__cfstring: 0x5ac0
-  __AUTH_CONST.__objc_const: 0xade0
+  __AUTH_CONST.__cfstring: 0x5ae0
+  __AUTH_CONST.__objc_const: 0xaf50
   __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_arrayobj: 0x108
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x218
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x224
   __DATA.__data: 0x908
-  __DATA.__bss: 0x60
+  __DATA.__bss: 0x68
   __DATA_DIRTY.__objc_data: 0xf00
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x80
+  __DATA_DIRTY.__bss: 0x78
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1D8F0455-2F97-3094-9159-9F63615303AB
-  Functions: 1965
-  Symbols:   6509
-  CStrings:  4179
+  UUID: 10654977-D251-353D-978B-666E3EBFE737
+  Functions: 1998
+  Symbols:   6601
+  CStrings:  4225
 
Symbols:
+ +[IXAppInstallCoordinator(IXOSModuleRegistration) registerContentsForOSModuleAtURL:options:error:]
+ +[IXAppInstallCoordinator(IXOSModuleRegistration) registerContentsForOSModuleAtURL:options:error:].cold.1
+ +[IXAppInstallCoordinator(IXOSModuleRegistration) setKnownOSModuleURLs:options:error:]
+ +[IXAppInstallCoordinator(IXOSModuleRegistration) setKnownOSModuleURLs:options:error:].cold.1
+ +[IXAppInstallCoordinator(IXOSModuleRegistration) unregisterContentsForOSModuleAtURL:options:error:]
+ +[IXAppInstallCoordinator(IXOSModuleRegistration) unregisterContentsForOSModuleAtURL:options:error:].cold.1
+ -[IXAppInstallObserver _client_mayUninstallAppWithIdentity:]
+ -[IXUnregisterOSModuleToken .cxx_destruct]
+ -[IXUnregisterOSModuleToken dealloc]
+ -[IXUnregisterOSModuleToken dealloc].cold.1
+ -[IXUnregisterOSModuleToken initWithModuleURL:options:]
+ -[IXUnregisterOSModuleToken invalidate]
+ -[IXUnregisterOSModuleToken isValid]
+ -[IXUnregisterOSModuleToken moduleURL]
+ -[IXUnregisterOSModuleToken options]
+ -[IXUnregisterOSModuleToken setIsValid:]
+ -[IXUnregisterOSModuleToken setModuleURL:]
+ -[IXUnregisterOSModuleToken setOptions:]
+ _OBJC_CLASS_$_IXUnregisterOSModuleToken
+ _OBJC_IVAR_$_IXUnregisterOSModuleToken._isValid
+ _OBJC_IVAR_$_IXUnregisterOSModuleToken._moduleURL
+ _OBJC_IVAR_$_IXUnregisterOSModuleToken._options
+ _OBJC_METACLASS_$_IXUnregisterOSModuleToken
+ __OBJC_$_CLASS_METHODS_IXAppInstallCoordinator(IXTesting|IXPersonaBasedMultiUser|IXDiskImageMounter|IXSimpleInstaller|IXSimpleInstallerPrivate|IXOSModuleRegistration|IXDemoteToPlaceholder|IXDemoteToPlaceholderTesting)
+ __OBJC_$_INSTANCE_METHODS_IXUnregisterOSModuleToken
+ __OBJC_$_INSTANCE_VARIABLES_IXUnregisterOSModuleToken
+ __OBJC_$_PROP_LIST_IXUnregisterOSModuleToken
+ __OBJC_CLASS_RO_$_IXUnregisterOSModuleToken
+ __OBJC_METACLASS_RO_$_IXUnregisterOSModuleToken
+ ___100+[IXAppInstallCoordinator(IXOSModuleRegistration) unregisterContentsForOSModuleAtURL:options:error:]_block_invoke
+ ___100+[IXAppInstallCoordinator(IXOSModuleRegistration) unregisterContentsForOSModuleAtURL:options:error:]_block_invoke.4
+ ___100+[IXAppInstallCoordinator(IXOSModuleRegistration) unregisterContentsForOSModuleAtURL:options:error:]_block_invoke.4.cold.1
+ ___100+[IXAppInstallCoordinator(IXOSModuleRegistration) unregisterContentsForOSModuleAtURL:options:error:]_block_invoke.cold.1
+ ___60-[IXAppInstallObserver _client_mayUninstallAppWithIdentity:]_block_invoke
+ ___86+[IXAppInstallCoordinator(IXOSModuleRegistration) setKnownOSModuleURLs:options:error:]_block_invoke
+ ___86+[IXAppInstallCoordinator(IXOSModuleRegistration) setKnownOSModuleURLs:options:error:]_block_invoke.6
+ ___86+[IXAppInstallCoordinator(IXOSModuleRegistration) setKnownOSModuleURLs:options:error:]_block_invoke.6.cold.1
+ ___86+[IXAppInstallCoordinator(IXOSModuleRegistration) setKnownOSModuleURLs:options:error:]_block_invoke.cold.1
+ ___98+[IXAppInstallCoordinator(IXOSModuleRegistration) registerContentsForOSModuleAtURL:options:error:]_block_invoke
+ ___98+[IXAppInstallCoordinator(IXOSModuleRegistration) registerContentsForOSModuleAtURL:options:error:]_block_invoke.2
+ ___98+[IXAppInstallCoordinator(IXOSModuleRegistration) registerContentsForOSModuleAtURL:options:error:]_block_invoke.2.cold.1
+ ___98+[IXAppInstallCoordinator(IXOSModuleRegistration) registerContentsForOSModuleAtURL:options:error:]_block_invoke.cold.1
+ ___block_descriptor_64_e8_32s40s48r56r_e20_v20?0B8"NSError"12lr48l8s32l8s40l8r56l8
+ _interface.weakInterface.336
+ _objc_msgSend$_remote_registerContentForOSModuleAtURL:options:completion:
+ _objc_msgSend$_remote_setKnownOSModuleURLs:options:completion:
+ _objc_msgSend$_remote_unregisterContentForOSModuleAtURL:options:completion:
+ _objc_msgSend$initWithModuleURL:options:
+ _objc_msgSend$mayUninstallAppWithIdentity:
+ _objc_msgSend$moduleURL
- __OBJC_$_CLASS_METHODS_IXAppInstallCoordinator(IXTesting|IXPersonaBasedMultiUser|IXDiskImageMounter|IXSimpleInstaller|IXSimpleInstallerPrivate|IXDemoteToPlaceholder|IXDemoteToPlaceholderTesting)
- _interface.weakInterface.330
CStrings:
+ "%s: Failed to register contents for OSModule at %@ : %@"
+ "%s: Failed to set known OSModule URLs to %@ : %@"
+ "%s: Failed to unregister contents for OSModule at %@ : %@"
+ "%s: IXUnregisterOSModuleToken deallocated without being invalidated for OSModule at %@"
+ "%s: Invalidated unregister token for OSModule at %@"
+ "%s: Successfully unregistered contents for OSModule at %@"
+ "%s: The options parameter passed to %s must be nil. : %@"
+ "%s: Token for OSModule at %@ already invalidated"
+ "+[IXAppInstallCoordinator(IXOSModuleRegistration) registerContentsForOSModuleAtURL:options:error:]"
+ "+[IXAppInstallCoordinator(IXOSModuleRegistration) registerContentsForOSModuleAtURL:options:error:]_block_invoke"
+ "+[IXAppInstallCoordinator(IXOSModuleRegistration) setKnownOSModuleURLs:options:error:]"
+ "+[IXAppInstallCoordinator(IXOSModuleRegistration) setKnownOSModuleURLs:options:error:]_block_invoke"
+ "+[IXAppInstallCoordinator(IXOSModuleRegistration) unregisterContentsForOSModuleAtURL:options:error:]"
+ "+[IXAppInstallCoordinator(IXOSModuleRegistration) unregisterContentsForOSModuleAtURL:options:error:]_block_invoke"
+ "-[IXAppInstallObserver _client_mayUninstallAppWithIdentity:]"
+ "-[IXAppInstallObserver _client_mayUninstallAppWithIdentity:]_block_invoke"
+ "-[IXUnregisterOSModuleToken dealloc]"
+ "-[IXUnregisterOSModuleToken invalidate]"
+ "@"
+ "IXOSModuleRegistration"
+ "IXUnregisterOSModuleToken"
+ "MayUninstallAppWithIdentity"
+ "T@\"NSURL\",C,N,V_moduleURL"
+ "T@,&,N,V_options"
+ "TB,N,V_isValid"
+ "The options parameter passed to %s must be nil."
+ "_client_mayUninstallAppWithIdentity:"
+ "_isValid"
+ "_moduleURL"
+ "_options"
+ "_remote_registerContentForOSModuleAtURL:options:completion:"
+ "_remote_setKnownOSModuleURLs:options:completion:"
+ "_remote_unregisterContentForOSModuleAtURL:options:completion:"
+ "initWithModuleURL:options:"
+ "isValid"
+ "mayUninstallAppWithIdentity:"
+ "moduleURL"
+ "options"
+ "registerContentsForOSModuleAtURL:options:error:"
+ "setIsValid:"
+ "setKnownOSModuleURLs:options:error:"
+ "setModuleURL:"
+ "setOptions:"
+ "unregisterContentsForOSModuleAtURL:options:error:"
+ "v40@0:8@\"NSSet\"16@24@?<v@?B@\"NSError\">32"

```
