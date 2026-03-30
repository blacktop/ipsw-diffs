## CoreServices

> `/System/Library/Frameworks/CoreServices.framework/CoreServices`

```diff

-1444.4.19.0.0
-  __TEXT.__text: 0x1b28e0
+1444.5.2.0.0
+  __TEXT.__text: 0x1b2b80
   __TEXT.__auth_stubs: 0x30b0
   __TEXT.__delay_stubs: 0x40
   __TEXT.__delay_helper: 0x180
   __TEXT.__objc_methlist: 0xcd54
   __TEXT.__const: 0x910
-  __TEXT.__cstring: 0x261da
-  __TEXT.__oslogstring: 0x13b8a
-  __TEXT.__gcc_except_tab: 0x278e8
+  __TEXT.__cstring: 0x2621e
+  __TEXT.__oslogstring: 0x13c30
+  __TEXT.__gcc_except_tab: 0x27938
   __TEXT.__ustring: 0x23c
-  __TEXT.__unwind_info: 0xb408
+  __TEXT.__unwind_info: 0xb420
   __TEXT.__objc_classname: 0x1f0e
   __TEXT.__objc_methname: 0x1d256
   __TEXT.__objc_methtype: 0xaa84

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 3AEB1510-47D7-3E7F-836A-73D696ECA05B
-  Functions: 8755
-  Symbols:   28641
-  CStrings:  13698
+  UUID: BD8A253C-E98A-32FB-B4F5-A2DAFBE64874
+  Functions: 8756
+  Symbols:   28645
+  CStrings:  13700
 
Symbols:
+ ___54-[_LSDOpenClient openAppLink:state:completionHandler:]_block_invoke_2
Functions:
~ +[LSAppLink(Internal) _appLinksWithState:context:limit:error:] : 748 -> 736
~ +[LSAppLink(Private) URLComponentsAreValidForAppLinks:error:] : 592 -> 608
~ -[_LSDOpenClient openAppLink:state:completionHandler:] : 1032 -> 1040
~ ___54-[_LSDOpenClient openAppLink:state:completionHandler:]_block_invoke : 24 -> 252
+ ___54-[_LSDOpenClient openAppLink:state:completionHandler:]_block_invoke_2
~ ___UTTypeCopyChildIdentifiers_block_invoke : 128 -> 152
CStrings:
+ "-[_LSDOpenClient openAppLink:state:completionHandler:]_block_invoke"
+ "error opening app link %{private}@ is being swallowed for pid %d because it cannot map the LS database. Error was %@. It will be replaced by one that is less useful."
+ "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /Library/Caches/com.apple.xbs/14B1BFD6-6C07-4078-9A16-8183BE16E619/TemporaryDirectory.XiH6T8/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1433:63)]"
+ "void LaunchServices::UTTypeEnumerateFlavoredDisplayNames(__strong LSDatabaseRef, const _UTTypeData *, const F &) [F = (lambda at /Library/Caches/com.apple.xbs/14B1BFD6-6C07-4078-9A16-8183BE16E619/TemporaryDirectory.XiH6T8/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Database/UTTypeCore.mm:159:55)]"
- "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /Library/Caches/com.apple.xbs/AA55923E-C55D-465C-A43A-FFF85059D9BE/TemporaryDirectory.vvSIkJ/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1433:63)]"
- "void LaunchServices::UTTypeEnumerateFlavoredDisplayNames(__strong LSDatabaseRef, const _UTTypeData *, const F &) [F = (lambda at /Library/Caches/com.apple.xbs/AA55923E-C55D-465C-A43A-FFF85059D9BE/TemporaryDirectory.vvSIkJ/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Database/UTTypeCore.mm:159:55)]"

```
