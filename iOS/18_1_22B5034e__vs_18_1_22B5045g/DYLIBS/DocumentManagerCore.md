## DocumentManagerCore

> `/System/Library/PrivateFrameworks/DocumentManagerCore.framework/DocumentManagerCore`

```diff

-336.0.0.0.0
-  __TEXT.__text: 0x2c8a0
+337.2.1.1.0
+  __TEXT.__text: 0x2d8c0
   __TEXT.__auth_stubs: 0x9c0
-  __TEXT.__objc_methlist: 0x2874
+  __TEXT.__objc_methlist: 0x292c
   __TEXT.__const: 0x4c6
   __TEXT.__gcc_except_tab: 0x688
-  __TEXT.__cstring: 0x33f1
-  __TEXT.__oslogstring: 0x2798
+  __TEXT.__cstring: 0x3521
+  __TEXT.__oslogstring: 0x2bd5
   __TEXT.__ustring: 0x10c
   __TEXT.__swift5_typeref: 0x8d
   __TEXT.__constg_swiftt: 0x90

   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_proto: 0x44
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0xd50
-  __TEXT.__eh_frame: 0x198
-  __TEXT.__objc_classname: 0x571
-  __TEXT.__objc_methname: 0x8366
+  __TEXT.__unwind_info: 0xd68
+  __TEXT.__eh_frame: 0x170
+  __TEXT.__objc_classname: 0x583
+  __TEXT.__objc_methname: 0x8786
   __TEXT.__objc_methtype: 0xd4a
-  __TEXT.__objc_stubs: 0x5ba0
+  __TEXT.__objc_stubs: 0x5e60
   __DATA_CONST.__got: 0x490
-  __DATA_CONST.__const: 0x13b8
+  __DATA_CONST.__const: 0x13d8
   __DATA_CONST.__objc_classlist: 0x128
-  __DATA_CONST.__objc_catlist: 0x50
+  __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2000
+  __DATA_CONST.__objc_selrefs: 0x20b0
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__auth_got: 0x4f0
   __AUTH_CONST.__auth_ptr: 0x118
   __AUTH_CONST.__const: 0x740
-  __AUTH_CONST.__cfstring: 0x2880
-  __AUTH_CONST.__objc_const: 0x62d0
+  __AUTH_CONST.__cfstring: 0x28c0
+  __AUTH_CONST.__objc_const: 0x63f8
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_ivar: 0x26c
-  __DATA.__data: 0x7c0
+  __DATA.__objc_ivar: 0x27c
+  __DATA.__data: 0x7b8
   __DATA.__bss: 0xa40
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0xbb0
-  __DATA_DIRTY.__data: 0x30
+  __DATA_DIRTY.__data: 0x28
   __DATA_DIRTY.__bss: 0xd8
   __DATA_DIRTY.__common: 0x98
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1314
-  Symbols:   1691
-  CStrings:  2257
+  Functions: 1342
+  Symbols:   1719
+  CStrings:  2307
 
CStrings:
+ "-[DOCAppProtectionManager _applicationRecordsForAPApplications:]"
+ "setAllProtectedApplications:"
+ "T@\"NSArray\",&,V_hiddenFilteredDocumentApplications"
+ "_allProtectedApplications"
+ "isFileSharingEnabled"
+ "[PROTECTED APPS] %!s(MISSING) applicationsWithContentHiddenFromSearch is NOT equal to lockedApplications"
+ "_lockedFilteredDocumentApplications"
+ "-[DOCAppProtectionManager filterApplications:]"
+ "updateCachedFilteredApplicationsIfNeeded"
+ "[PROTECTED APPS] %!s(MISSING) posting notification: %!@(MISSING) with: %!l(MISSING)u changed apps: %!@(MISSING)"
+ "infoDictionary"
+ "[PROTECTED APPS] %!s(MISSING) could not find cached app for ID: %!@(MISSING) in appContainer having app cache"
+ "[PROTECTED APPS] %!s(MISSING) found relevant: %!l(MISSING)u applications and excluded: %!l(MISSING)u applications"
+ "_applicationRecordsForAPApplications:"
+ "T@\"NSArray\",&,V_filteredDocumentApplicationsWithContentHiddenFromSearch"
+ "objectForKey:ofClass:"
+ "-[DOCAppProtectionManager updateCachedFilteredApplications]"
+ "T@\"NSSet\",&,V_allProtectedApplications"
+ "[PROTECTED APPS] %!s(MISSING) begin filtering lockedApplications: %!l(MISSING)u hiddenApplications: %!l(MISSING)u applicationsWithContentHiddenFromSearch: %!l(MISSING)u"
+ "\b"
+ "T@\"NSArray\",&,V_lockedFilteredDocumentApplications"
+ "[PROTECTED APPS] %!s(MISSING) could not get LSApplicationRecord for APApplication: %!@(MISSING)"
+ "com.apple.fileprovider-nonui"
+ "filterApplications:"
+ "updateCachedFilteredApplications"
+ "ProtectedApps_Filter_Cacahed_Applications"
+ "lockedFilteredDocumentApplications"
+ "[PROTECTED APPS] %!s(MISSING) applicationsWithContentHiddenFromSearch protected applications changed. Updating"
+ "hiddenFilteredDocumentApplications"
+ "doc_hasFileProviderExtension"
+ "[PROTECTED APPS] %!s(MISSING) begin updating filtered applications cache"
+ "_filteredDocumentApplicationsWithContentHiddenFromSearch"
+ "[PROTECTED APPS] %!s(MISSING) subjects (%!l(MISSING)u): %!@(MISSING) app monitor subscription: %!@(MISSING)"
+ "UISupportsDocumentBrowser"
+ "-[DOCAppProtectionManager updateCachedFilteredApplicationsIfNeeded]"
+ "doc_canHaveAppContainer"
+ "arrayWithArray:"
+ "setLockedFilteredDocumentApplications:"
+ "[PROTECTED APPS] %!s(MISSING) could not find protected app APApplication: %!@(MISSING) in app container cache"
+ "setFilteredDocumentApplicationsWithContentHiddenFromSearch:"
+ "[PROTECTED APPS] %!s(MISSING) cache is nil. Updating locked and hidden applications cache"
+ "filteredDocumentApplicationsWithContentHiddenFromSearch"
+ "[PROTECTED APPS] %!s(MISSING) LSApplicationRecord: %!@(MISSING) should NOT be included in the list of protected apps. APApplication: %!@(MISSING)"
+ "dictionaryWithDictionary:"
+ "allProtectedApplications"
+ "[PROTECTED APPS] %!s(MISSING) prepare to notify that: %!l(MISSING)u application(s) changed"
+ "_applicationShouldBeIncludedInList:"
+ "applicationExtensionRecords"
+ "extensionPointRecord"
+ "[PROTECTED APPS] %!s(MISSING) could not find protected app for APApplication: %!@(MISSING) in app container cache"
+ "_hiddenFilteredDocumentApplications"
+ "setHiddenFilteredDocumentApplications:"
- "[PROTECTED APPS] %!s(MISSING) subjects: %!@(MISSING) app monitor subscription: %!@(MISSING)"
- "[PROTECTED APPS] %!s(MISSING) posting notification: %!@(MISSING) with changed apps: %!@(MISSING)"
- "[PROTECTED APPS] %!s(MISSING) could not find cached app for ID: %!@(MISSING)"

```
