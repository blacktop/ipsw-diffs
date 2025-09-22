## NotesAnalytics

> `/System/Library/PrivateFrameworks/NotesAnalytics.framework/NotesAnalytics`

```diff

-2952.2.1.0.0
-  __TEXT.__text: 0x5f1f8
-  __TEXT.__auth_stubs: 0x770
-  __TEXT.__objc_methlist: 0xad04
-  __TEXT.__const: 0x140
-  __TEXT.__cstring: 0x6d37
-  __TEXT.__gcc_except_tab: 0xda4
+2952.40.7.0.0
+  __TEXT.__text: 0x5ed2c
+  __TEXT.__auth_stubs: 0x720
+  __TEXT.__delay_stubs: 0x2c
+  __TEXT.__delay_helper: 0x16c
+  __TEXT.__objc_methlist: 0xad1c
+  __TEXT.__const: 0x138
+  __TEXT.__cstring: 0x6d95
+  __TEXT.__gcc_except_tab: 0xd6c
   __TEXT.__oslogstring: 0xe20
-  __TEXT.__dlopen_cstrs: 0xcc
-  __TEXT.__unwind_info: 0x1e60
+  __TEXT.__unwind_info: 0x1e28
   __TEXT.__objc_classname: 0x26c2
-  __TEXT.__objc_methname: 0x1c54f
+  __TEXT.__objc_methname: 0x1c5c8
   __TEXT.__objc_methtype: 0x1cb0
-  __TEXT.__objc_stubs: 0xc800
-  __DATA_CONST.__got: 0xe48
-  __DATA_CONST.__const: 0x1420
+  __TEXT.__objc_stubs: 0xc860
+  __DATA_CONST.__got: 0xe58
+  __DATA_CONST.__const: 0x13f0
   __DATA_CONST.__objc_classlist: 0xbd0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3bf8
+  __DATA_CONST.__objc_selrefs: 0x3c18
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x7d0
   __DATA_CONST.__objc_arraydata: 0x2410
-  __AUTH_CONST.__auth_got: 0x3c8
+  __AUTH_CONST.__auth_got: 0x3a8
   __AUTH_CONST.__const: 0x220
   __AUTH_CONST.__cfstring: 0x9ea0
-  __AUTH_CONST.__objc_const: 0x1f2e8
+  __AUTH_CONST.__objc_const: 0x201b8
   __AUTH_CONST.__objc_intobj: 0x5cd0
   __AUTH_CONST.__objc_arrayobj: 0x318
   __AUTH_CONST.__objc_doubleobj: 0xa60
   __AUTH.__objc_data: 0x3598
   __DATA.__objc_ivar: 0xdac
-  __DATA.__data: 0x480
+  __DATA.__data: 0x488
   __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_data: 0x4088
-  __DATA_DIRTY.__bss: 0xf0
+  __DATA_DIRTY.__bss: 0xd0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/BackgroundTasks.framework/BackgroundTasks
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /System/Library/PrivateFrameworks/AppAnalytics.framework/AppAnalytics
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
+  - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/Notes.framework/Notes
   - /System/Library/PrivateFrameworks/NotesShared.framework/NotesShared
   - /System/Library/PrivateFrameworks/NotesSupport.framework/NotesSupport
   - /System/Library/PrivateFrameworks/NotesUI.framework/NotesUI
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/Synapse.framework/Synapse
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 682B7AE6-2140-3236-99A1-C06C4F8F144D
-  Functions: 3276
-  Symbols:   12909
+  UUID: 38E675E9-E9BA-3C1E-9832-198E9D7D51AE
+  Functions: 3270
+  Symbols:   12895
   CStrings:  6745
 
Symbols:
+ _DiagnosticLogSubmissionEnabled
+ _DiagnosticLogSubmissionEnabled$delayInitStub
+ _OBJC_CLASS_$_MCProfileConnection
+ _OBJC_CLASS_$_NSCharacterSet
+ _dlopen
+ _dlopenHelper$CrashReporterSupport
+ _dlopenHelper$ManagedConfiguration
+ _dlopenHelperFlag$CrashReporterSupport
+ _dlopenHelperFlag$ManagedConfiguration
+ _gotLoadHelper_x8$_OBJC_CLASS_$_MCProfileConnection
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$componentsSeparatedByCharactersInSet:
+ _objc_msgSend$whitespaceAndNewlineCharacterSet
- +[ICNAOptedInObject isOptedInForAnalytics].cold.2
- GCC_except_table261
- GCC_except_table5
- _CrashReporterSupportLibraryCore.frameworkLibrary
- _ManagedConfigurationLibraryCore.frameworkLibrary
- ___CrashReporterSupportLibraryCore_block_invoke
- ___ManagedConfigurationLibraryCore_block_invoke
- ___getDiagnosticLogSubmissionEnabledSymbolLoc_block_invoke
- ___getMCProfileConnectionClass_block_invoke
- ___getMCProfileConnectionClass_block_invoke.cold.1
- __sl_dlopen
- _abort_report_np
- _audit_stringCrashReporterSupport
- _audit_stringManagedConfiguration
- _dlerror
- _dlsym
- _free
- _getDiagnosticLogSubmissionEnabledSymbolLoc.ptr
- _getMCProfileConnectionClass.softClass
- _objc_getClass
CStrings:
+ "/System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport"
+ "/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration"
+ "componentsJoinedByString:"
+ "componentsSeparatedByCharactersInSet:"
+ "requiresTrackingConsent"
+ "whitespaceAndNewlineCharacterSet"
- "%s"
- "DiagnosticLogSubmissionEnabled"
- "MCProfileConnection"
- "Unable to find class %s"
- "softlink:r:path:/System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport"
- "softlink:r:path:/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration"

```
