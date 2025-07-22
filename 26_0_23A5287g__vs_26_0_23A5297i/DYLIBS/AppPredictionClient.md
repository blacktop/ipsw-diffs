## AppPredictionClient

> `/System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient`

```diff

-615.0.2.0.0
-  __TEXT.__text: 0x18c0d0
+617.0.0.0.0
+  __TEXT.__text: 0x18c6b8
   __TEXT.__auth_stubs: 0xf00
-  __TEXT.__objc_methlist: 0x18a64
+  __TEXT.__objc_methlist: 0x18a84
   __TEXT.__const: 0x6f8
-  __TEXT.__cstring: 0x1b74f
+  __TEXT.__cstring: 0x1b84e
   __TEXT.__oslogstring: 0x1746f
-  __TEXT.__gcc_except_tab: 0x22e0
-  __TEXT.__dlopen_cstrs: 0x3d0
+  __TEXT.__gcc_except_tab: 0x22fc
+  __TEXT.__dlopen_cstrs: 0x42d
   __TEXT.__ustring: 0x18a
-  __TEXT.__unwind_info: 0x66a0
+  __TEXT.__unwind_info: 0x66b0
   __TEXT.__objc_classname: 0x3be3
-  __TEXT.__objc_methname: 0x340ac
+  __TEXT.__objc_methname: 0x34135
   __TEXT.__objc_methtype: 0x676d
   __TEXT.__objc_stubs: 0x1cae0
-  __DATA_CONST.__got: 0x16f0
-  __DATA_CONST.__const: 0x6358
+  __DATA_CONST.__got: 0x16f8
+  __DATA_CONST.__const: 0x6370
   __DATA_CONST.__objc_classlist: 0xe48
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9e90
+  __DATA_CONST.__objc_selrefs: 0x9ea8
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0xc50
   __DATA_CONST.__objc_arraydata: 0xaf8
   __AUTH_CONST.__auth_got: 0x790
   __AUTH_CONST.__const: 0x2a60
-  __AUTH_CONST.__cfstring: 0x15160
-  __AUTH_CONST.__objc_const: 0x45ce0
+  __AUTH_CONST.__cfstring: 0x15180
+  __AUTH_CONST.__objc_const: 0x45cf0
   __AUTH_CONST.__objc_intobj: 0xa38
   __AUTH_CONST.__objc_arrayobj: 0x6d8
   __AUTH_CONST.__objc_doubleobj: 0x10

   __AUTH.__objc_data: 0x3de0
   __DATA.__objc_ivar: 0x1c58
   __DATA.__data: 0x1cf0
-  __DATA.__bss: 0x378
+  __DATA.__bss: 0x390
   __DATA_DIRTY.__objc_data: 0x50f0
   __DATA_DIRTY.__data: 0x88
   __DATA_DIRTY.__bss: 0x2c8

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: D67788CE-64FD-39FC-919E-A146623EF02C
-  Functions: 10646
-  Symbols:   35045
-  CStrings:  15981
+  UUID: E79F413E-AFB7-373B-A033-4BABB8955627
+  Functions: 10656
+  Symbols:   35071
+  CStrings:  15992
 
Symbols:
+ +[ATXAppDisplayIdentifiers _processIdentifiersFromEnumerator:intoSet:includeInternalMacOSApps:]
+ +[ATXSpotlightEvent(Initializers) documentSuggestionDismissedWithPaths:date:]
+ -[ATXActionCriteriaWorldState airplaneMode].cold.1
+ -[ATXActionCriteriaWorldState airplaneMode].cold.2
+ -[ATXMenuItemInvocation initWithIdentity:invocationType:sourceType:localizedKeyboardShortcutDisplayName:]
+ -[ATXMenuItemInvocation localizedKeyboardShortcutDisplayName]
+ _OBJC_IVAR_$_ATXMenuItemInvocation._localizedKeyboardShortcutDisplayName
+ _SystemConfigurationLibrary
+ _SystemConfigurationLibrary.cold.1
+ _SystemConfigurationLibraryCore.frameworkLibrary
+ ___48+[ATXContactModeEntity vipContactEmailAddresses]_block_invoke.374
+ ___48+[ATXContactModeEntity vipContactEmailAddresses]_block_invoke.374.cold.1
+ ___SystemConfigurationLibraryCore_block_invoke
+ ___getSCPreferencesCreateSymbolLoc_block_invoke
+ ___getSCPreferencesGetValueSymbolLoc_block_invoke
+ _audit_stringSystemConfiguration
+ _getSCPreferencesCreateSymbolLoc.ptr
+ _getSCPreferencesGetValueSymbolLoc.ptr
+ _kCFBooleanTrue
+ _objc_msgSend$initWithIdentity:invocationType:sourceType:localizedKeyboardShortcutDisplayName:
+ _objc_msgSend$localizedKeyboardShortcutDisplayName
- +[ATXAppDisplayIdentifiers _processIdentifiersFromEnumerator:intoSet:withSupportedAppPaths:includeInternalMacOSApps:]
- _OBJC_IVAR_$_ATXMenuItemInvocation._localizedKeyboardShorctcutDisplayName
- ___48+[ATXContactModeEntity vipContactEmailAddresses]_block_invoke.377
- ___48+[ATXContactModeEntity vipContactEmailAddresses]_block_invoke.377.cold.1
- _objc_msgSend$initWithIdentity:invocationType:sourceType:localizedKeyboardShorctcutDisplayName:
- _objc_msgSend$localizedKeyboardShorctcutDisplayName
CStrings:
+ "CFPropertyListRef _SCPreferencesGetValue(SCPreferencesRef, CFStringRef)"
+ "SCPreferencesCreate"
+ "SCPreferencesGetValue"
+ "SCPreferencesRef _SCPreferencesCreate(CFAllocatorRef, CFStringRef, CFStringRef)"
+ "T@\"NSString\",R,N,V_localizedKeyboardShortcutDisplayName"
+ "_localizedKeyboardShortcutDisplayName"
+ "_processIdentifiersFromEnumerator:intoSet:includeInternalMacOSApps:"
+ "com.apple.radios.plist"
+ "documentSuggestionDismissedWithPaths:date:"
+ "initWithIdentity:invocationType:sourceType:localizedKeyboardShortcutDisplayName:"
+ "localizedKeyboardShortcutDisplayName"
+ "softlink:r:path:/System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration"
+ "void *SystemConfigurationLibrary(void)"
- "T@\"NSString\",R,N,V_localizedKeyboardShorctcutDisplayName"
- "_localizedKeyboardShorctcutDisplayName"
- "_processIdentifiersFromEnumerator:intoSet:withSupportedAppPaths:includeInternalMacOSApps:"

```
