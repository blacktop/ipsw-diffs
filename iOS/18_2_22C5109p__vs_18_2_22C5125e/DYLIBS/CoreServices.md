## CoreServices

> `/System/Library/Frameworks/CoreServices.framework/CoreServices`

```diff

-1367.1.0.0.0
-  __TEXT.__text: 0x18c800
-  __TEXT.__auth_stubs: 0x3200
-  __TEXT.__objc_methlist: 0xb070
-  __TEXT.__const: 0x8f0
-  __TEXT.__cstring: 0x1fa77
-  __TEXT.__oslogstring: 0x1279f
-  __TEXT.__gcc_except_tab: 0x22c30
+1367.4.0.0.0
+  __TEXT.__text: 0x18fbc0
+  __TEXT.__auth_stubs: 0x3210
+  __TEXT.__objc_methlist: 0xb240
+  __TEXT.__const: 0x900
+  __TEXT.__cstring: 0x1fca3
+  __TEXT.__oslogstring: 0x12a04
+  __TEXT.__gcc_except_tab: 0x23264
   __TEXT.__ustring: 0x23c
-  __TEXT.__unwind_info: 0x9fe0
+  __TEXT.__unwind_info: 0xa148
   __TEXT.__eh_frame: 0x60
-  __TEXT.__objc_classname: 0x1b7a
-  __TEXT.__objc_methname: 0x1b2f9
-  __TEXT.__objc_methtype: 0xa90e
-  __TEXT.__objc_stubs: 0xef80
-  __DATA_CONST.__got: 0x9e8
-  __DATA_CONST.__const: 0x6730
-  __DATA_CONST.__objc_classlist: 0x610
+  __TEXT.__objc_classname: 0x1cb6
+  __TEXT.__objc_methname: 0x1b6b8
+  __TEXT.__objc_methtype: 0xaa7d
+  __TEXT.__objc_stubs: 0xf1a0
+  __DATA_CONST.__got: 0x9f0
+  __DATA_CONST.__const: 0x6788
+  __DATA_CONST.__objc_classlist: 0x640
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x130
+  __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5830
+  __DATA_CONST.__objc_selrefs: 0x58d8
   __DATA_CONST.__objc_protorefs: 0x98
-  __DATA_CONST.__objc_superrefs: 0x4d0
-  __DATA_CONST.__objc_arraydata: 0x178
-  __AUTH_CONST.__auth_got: 0x1918
+  __DATA_CONST.__objc_superrefs: 0x4e8
+  __DATA_CONST.__objc_arraydata: 0x188
+  __AUTH_CONST.__auth_got: 0x1920
   __AUTH_CONST.__auth_ptr: 0x48
-  __AUTH_CONST.__const: 0x3288
-  __AUTH_CONST.__cfstring: 0x15a60
-  __AUTH_CONST.__objc_const: 0x130a8
+  __AUTH_CONST.__const: 0x3380
+  __AUTH_CONST.__cfstring: 0x15c20
+  __AUTH_CONST.__objc_const: 0x13808
   __AUTH_CONST.__objc_intobj: 0x780
+  __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0xc0
-  __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH.__objc_data: 0x2620
+  __AUTH.__objc_data: 0x2800
   __AUTH.__data: 0x320
-  __DATA.__objc_ivar: 0x9b0
-  __DATA.__data: 0x1250
-  __DATA.__bss: 0xed0
+  __DATA.__objc_ivar: 0x9d4
+  __DATA.__data: 0x1350
+  __DATA.__bss: 0xee8
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x1680
-  __DATA_DIRTY.__data: 0x98
+  __DATA_DIRTY.__data: 0x58
   __DATA_DIRTY.__crash_info: 0x40
-  __DATA_DIRTY.__bss: 0x7d0
+  __DATA_DIRTY.__bss: 0x7c8
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 7831
-  Symbols:   9534
-  CStrings:  10074
+  Functions: 7903
+  Symbols:   9611
+  CStrings:  10159
 
Symbols:
+ _MGGetBoolAnswer
+ _OBJC_CLASS_$_LSDefaultApplicationQueryResult
+ _OBJC_METACLASS_$_LSDefaultApplicationQueryResult
CStrings:
+ "%!s(MISSING)entry for app %!@(MISSING) in category %!l(MISSING)u"
+ "%!{(MISSING)public}@: clearing entries for %!@(MISSING)"
+ "-[_LSDReadClient getCurrentApplicationDefaultInfoForCategory:completion:]"
+ "<%!@(MISSING)@%!p(MISSING): referenceDate %!@(MISSING) didRefresh %!d(MISSING) refreshAfter %!@(MISSING) defaultForCategory %!d(MISSING)>"
+ "@\"<LSDefaultApplicationQueryDatastore>\""
+ "@\"<LSDefaultApplicationQueryDefaultAppEvaluator>\""
+ "@\"LSDefaultApplicationQueryEntry\"32@0:8@\"LSApplicationRecord\"16Q24"
+ "@\"NSURL\"24@0:8Q16"
+ "@40@0:8@16B24@28B36"
+ "App not a candidate for this category, so will never be the default"
+ "Couldn't save default application query state after removing %!@(MISSING): %!@(MISSING)"
+ "Couldn't save default application query state: %!@(MISSING)"
+ "Couldn't write state plist to %!@(MISSING): %!@(MISSING)"
+ "DefaultAppQueryState.plist"
+ "FaceTime is not a candidate for default calling app on this device."
+ "IsDefault"
+ "LSDefaultApplicationQueryBackend"
+ "LSDefaultApplicationQueryDatabaseDefaultAppEvaluator"
+ "LSDefaultApplicationQueryDatastore"
+ "LSDefaultApplicationQueryDefaultAppEvaluator"
+ "LSDefaultApplicationQueryEntry"
+ "LSDefaultApplicationQueryResult"
+ "LSDefaultApplicationQueryServerDatastore"
+ "LSDefaultApplicationQueryServerStateManager saved state with error %!@(MISSING)"
+ "LSDefaultApplicationQueryUnrestrictedBehavior"
+ "NSString *LSDefaultAppCategoryCopyName(LSDefaultAppCategory)"
+ "No best app for %!@(MISSING): %!@(MISSING)"
+ "Refresh"
+ "T@\"NSDate\",R,N,V_referenceDate"
+ "T@\"NSDate\",R,N,V_refreshAfter"
+ "T@\"NSDate\",R,N,V_refreshDate"
+ "T@\"NSDate\",R,N,V_windowOpenDate"
+ "TB,R,N,GisDefaultForCategory,V_defaultForCategory"
+ "TB,R,N,V_didRefresh"
+ "URLOfDefaultAppForCategory:"
+ "_datastore"
+ "_defaultAppEvaluator"
+ "_defaultForCategory"
+ "_didRefresh"
+ "_isApp:defaultForCategory:"
+ "_referenceDate"
+ "_refreshAfter"
+ "_refreshDate"
+ "_windowOpenDate"
+ "bogus app category %!l(MISSING)u"
+ "com.apple.FaceTime"
+ "com.apple.lsd.defaultappquery.save"
+ "couldn't make query entry from category dict %!@(MISSING)!"
+ "createFromPlistRepresentation:"
+ "defaultAppQueryStateURL"
+ "defaultForCategory"
+ "didRefresh"
+ "entryForApplication:category:"
+ "getCurrentApplicationDefaultInfoForCategory:completion:"
+ "green-tea"
+ "initWithDatastore:defaultAppEvaluator:"
+ "initWithReferenceDate:didRefresh:refreshAfter:defaultForCategory:"
+ "initWithWindowOpenDate:refreshDate:defaultForCategory:"
+ "isDefaultForCategory"
+ "no "
+ "opened new window at %!@(MISSING), returning %!@(MISSING)"
+ "pid %!l(MISSING)d getting app default info for category %!l(MISSING)u"
+ "plistRepresentation"
+ "process is not an app"
+ "queryResultForCategory:error:"
+ "referenceDate"
+ "refreshAfter"
+ "refreshDate"
+ "refreshQueryResultForApplication:category:"
+ "refreshed open window at %!@(MISSING), returning %!@(MISSING)"
+ "removeEntriesForBundleIdentifier:"
+ "saveToDisk"
+ "setEntry:forApplication:category:"
+ "stale window, returning %!@(MISSING)"
+ "timeIntervalSinceDate:"
+ "v24@0:8@\"NSString\"16"
+ "v24@?0@\"LSDefaultApplicationQueryResult\"8@\"NSError\"16"
+ "v32@0:8Q16@?<v@?@\"LSDefaultApplicationQueryResult\"@\"NSError\">24"
+ "v40@0:8@\"LSDefaultApplicationQueryEntry\"16@\"LSApplicationRecord\"24Q32"
+ "v40@0:8@16@24Q32"
+ "window open date %!@(MISSING)"
+ "windowOpenDate"

```
