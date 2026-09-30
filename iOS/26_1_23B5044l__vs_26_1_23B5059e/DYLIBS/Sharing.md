## Sharing

> `/System/Library/PrivateFrameworks/Sharing.framework/Sharing`

```diff

-2094.20.31.2.1
-  __TEXT.__text: 0x30691c
+2094.20.65.0.0
+  __TEXT.__text: 0x3070bc
   __TEXT.__auth_stubs: 0x4b40
-  __TEXT.__objc_methlist: 0x1439c
+  __TEXT.__objc_methlist: 0x1440c
   __TEXT.__const: 0x1c784
-  __TEXT.__cstring: 0x3b5d6
-  __TEXT.__gcc_except_tab: 0x3488
-  __TEXT.__oslogstring: 0x972e
+  __TEXT.__cstring: 0x3b706
+  __TEXT.__gcc_except_tab: 0x349c
+  __TEXT.__oslogstring: 0x976e
   __TEXT.__dlopen_cstrs: 0x640
   __TEXT.__ustring: 0xf0
   __TEXT.__swift5_typeref: 0x7d6a

   __TEXT.__swift_as_entry: 0x338
   __TEXT.__swift_as_ret: 0x338
   __TEXT.__swift5_mpenum: 0xa8
-  __TEXT.__unwind_info: 0xcc48
+  __TEXT.__unwind_info: 0xcc58
   __TEXT.__eh_frame: 0xbc10
   __TEXT.__objc_classname: 0x1ecb
-  __TEXT.__objc_methname: 0x2cf76
-  __TEXT.__objc_methtype: 0x5e72
-  __TEXT.__objc_stubs: 0x18920
+  __TEXT.__objc_methname: 0x2d111
+  __TEXT.__objc_methtype: 0x5eb4
+  __TEXT.__objc_stubs: 0x18a40
   __DATA_CONST.__got: 0x11f0
-  __DATA_CONST.__const: 0x75d0
+  __DATA_CONST.__const: 0x75c0
   __DATA_CONST.__objc_classlist: 0x848
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x3d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x96f0
+  __DATA_CONST.__objc_selrefs: 0x9748
   __DATA_CONST.__objc_protorefs: 0x1e8
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x538
   __DATA_CONST.__objc_arraydata: 0x448
   __AUTH_CONST.__auth_got: 0x25b8
   __AUTH_CONST.__const: 0x13c88
-  __AUTH_CONST.__cfstring: 0x13960
-  __AUTH_CONST.__objc_const: 0x38d40
+  __AUTH_CONST.__cfstring: 0x13a00
+  __AUTH_CONST.__objc_const: 0x38dd8
   __AUTH_CONST.__objc_intobj: 0x660
   __AUTH_CONST.__objc_dictobj: 0x5c8
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH.__objc_data: 0x2a60
   __AUTH.__data: 0x2588
-  __DATA.__objc_ivar: 0x257c
-  __DATA.__data: 0xbc28
+  __DATA.__objc_ivar: 0x2588
+  __DATA.__data: 0xbbf8
   __DATA.__bss: 0x342a0
   __DATA.__common: 0xb0
   __DATA_DIRTY.__objc_data: 0x4258
-  __DATA_DIRTY.__data: 0x1330
+  __DATA_DIRTY.__data: 0x1370
   __DATA_DIRTY.__bss: 0x2d8
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0E3A5146-082F-3A61-8337-50CEF2F5C6DA
-  Functions: 20895
-  Symbols:   38076
-  CStrings:  19995
+  UUID: E740BDFE-D4DE-3F2A-92C2-CAE267644A31
+  Functions: 20902
+  Symbols:   38109
+  CStrings:  20026
 
Symbols:
+ -[SFAppleIDClient _altDSIDLookupWithEmails:phoneNumbers:completion:]
+ -[SFAppleIDClient altDSIDLookupWithEmails:phoneNumbers:completion:]
+ -[SFHeadphoneProduct isAirPodsPro]
+ -[SFHeadphoneProduct setIsAirPodsPro:]
+ -[SFShareSheetSessionModeTestingSnapshot _removeShortcutsFromDiscoveredActivities:]
+ -[SFShareSheetSessionTestingSnapshot setTestName:]
+ -[SFShareSheetSessionTestingSnapshot setTestSuiteName:]
+ -[SFShareSheetSessionTestingSnapshot testName]
+ -[SFShareSheetSessionTestingSnapshot testSuiteName]
+ -[SFShareSheetSessionTestingSnapshot updatePreconditionsIfNeededWithReferenceSnapshot:]
+ GCC_except_table46
+ GCC_except_table70
+ _OBJC_IVAR_$_SFHeadphoneProduct._isAirPodsPro
+ _OBJC_IVAR_$_SFShareSheetSessionTestingSnapshot._testName
+ _OBJC_IVAR_$_SFShareSheetSessionTestingSnapshot._testSuiteName
+ ___67-[SFAppleIDClient altDSIDLookupWithEmails:phoneNumbers:completion:]_block_invoke
+ ___68-[SFAppleIDClient _altDSIDLookupWithEmails:phoneNumbers:completion:]_block_invoke
+ ___68-[SFAppleIDClient _altDSIDLookupWithEmails:phoneNumbers:completion:]_block_invoke_2
+ ___block_literal_global.364
+ _keypath_set.80Tm
+ _objc_msgSend$_altDSIDLookupWithEmails:phoneNumbers:completion:
+ _objc_msgSend$_removeShortcutsFromDiscoveredActivities:
+ _objc_msgSend$altDSIDLookupWithEmails:phoneNumbers:completion:
+ _objc_msgSend$filterUsingPredicate:
+ _objc_msgSend$isAirPodsPro
+ _objc_msgSend$nsExtensionAttributes
+ _objc_msgSend$setIsAirPodsPro:
+ _objc_msgSend$testName
+ _objc_msgSend$testSuiteName
- -[SFShareSheetSessionTestingSnapshot updatePreconditionsIfNeeded]
- _OUTLINED_FUNCTION_32
- _OUTLINED_FUNCTION_33
- ___block_literal_global.342
- _keypath_set.83Tm
CStrings:
+ "NOT SELF BEGINSWITH 'com.apple.shortcuts.Run-Workflow'"
+ "ShareSheetSnapshot-%@"
+ "Sharing/SFAppleIDClient/altDSIDLookupWithEmailsAndPhoneNumbers"
+ "T@\"NSString\",C,N,V_testName"
+ "T@\"NSString\",C,N,V_testSuiteName"
+ "TB,N,V_isAirPodsPro"
+ "__privacyImprovements"
+ "_altDSIDLookupWithEmails:phoneNumbers:completion:"
+ "_isAirPodsPro"
+ "_removeShortcutsFromDiscoveredActivities:"
+ "_testName"
+ "_testSuiteName"
+ "altDSIDLookupWithEmails:phoneNumbers:completion:"
+ "com.apple.sharing.AirDrop.privateAirDrop.handleRetryDelay"
+ "com.apple.sharing.AirDrop.privateAirDrop.killswitch"
+ "com.apple.sharing.AirDrop.privateAirDrop.requestBackoff"
+ "filterUsingPredicate:"
+ "isAirPodsPro"
+ "nsExtensionAttributes"
+ "setIsAirPodsPro:"
+ "setTestName:"
+ "setTestSuiteName:"
+ "testName"
+ "testSuiteName"
+ "updatePreconditionsIfNeededWithReferenceSnapshot:"
+ "v40@0:8@\"NSArray\"16@\"NSArray\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
- "_privacyImprovements"
- "updatePreconditionsIfNeeded"

```
