## NetAuthSysAgent

> `/System/Library/CoreServices/NetAuthAgent.app/Contents/MacOS/NetAuthSysAgent`

```diff

-  __TEXT.__text: 0x1864c
-  __TEXT.__auth_stubs: 0xcf0
-  __TEXT.__objc_stubs: 0x2520
-  __TEXT.__objc_methlist: 0x1020
+  __TEXT.__text: 0x190d4
+  __TEXT.__auth_stubs: 0xd10
+  __TEXT.__objc_stubs: 0x25a0
+  __TEXT.__objc_methlist: 0x1040
   __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x3775
-  __TEXT.__gcc_except_tab: 0x290
-  __TEXT.__objc_methname: 0x1f09
+  __TEXT.__cstring: 0x3975
+  __TEXT.__gcc_except_tab: 0x2a0
+  __TEXT.__objc_methname: 0x1f80
   __TEXT.__objc_classname: 0x15e
   __TEXT.__objc_methtype: 0x425
-  __TEXT.__unwind_info: 0x630
-  __DATA_CONST.__const: 0x770
-  __DATA_CONST.__cfstring: 0x37a0
+  __TEXT.__unwind_info: 0x670
+  __DATA_CONST.__const: 0x7c0
+  __DATA_CONST.__cfstring: 0x3860
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x40
-  __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x688
-  __DATA_CONST.__got: 0x2b0
+  __DATA_CONST.__objc_intobj: 0x30
+  __DATA_CONST.__auth_got: 0x698
+  __DATA_CONST.__got: 0x2b8
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA.__objc_const: 0xbc0
-  __DATA.__objc_selrefs: 0xaa0
-  __DATA.__objc_ivar: 0xb4
+  __DATA.__objc_const: 0xbe0
+  __DATA.__objc_selrefs: 0xac0
+  __DATA.__objc_ivar: 0xb8
   __DATA.__objc_data: 0x320
-  __DATA.__bss: 0xe0
+  __DATA.__bss: 0xf0
   __DATA.__common: 0x38
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 468
-  Symbols:   304
-  CStrings:  1367
+  Functions: 484
+  Symbols:   306
+  CStrings:  1385
 
Sections:
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_data : content changed
Symbols:
+ _CFBundleCopyBundleLocalizations
+ _CFBundleCopyResourceURLForLocalization
CStrings:
+ "B16@?0@\"NSMutableDictionary\"8"
+ "Backstop marker write failed for \"%@\": %d"
+ "Failed to enumerate NETWORK_PASSWORD localizations"
+ "GetCredentials: not marking server known (errorReported=%d, stage=%d, hasCredentials=%d, useGuest=%d)"
+ "Localizable.strings for \"%@\" failed to load as a property list"
+ "NetAuth description kinds across locales: %@"
+ "No NETWORK_PASSWORD localizations resolved; skipping Generic-password sweep and deferring migration"
+ "No matching keychain items"
+ "No new server markers to add; stamping migration version"
+ "Server markers migration %@"
+ "Server markers plist exists but is unreadable; starting fresh (data loss)"
+ "Server markers rename already at version %ld"
+ "SetKnownServerMarkersAsAccountUpdated: enter"
+ "Skipping marker container write because a keychain query failed (%d); migration will retry"
+ "Stamped server markers migration version %ld"
+ "Unable to write server markers: %@"
+ "_addKnownServerIfQualified"
+ "addKnownServer: marker write failed for \"%@\": %d"
+ "already complete"
+ "checkResourceIsReachableAndReturnError:"
+ "clearErrorReported"
+ "mErrorReported"
+ "needed"
+ "noteErrorReported"
+ "strings"
- "Creating an empty server markers dict"
- "Failed to get kind string"
- "No valid server markers found, creating empty container to mark migration complete"
- "Saving the server markers"
- "Server markers already migrated to %d"
- "Server markers dict loaded"
- "The server marker plist %@"
- "Unable to save the server markers"
- "Unable to save the server markers because of an error: %@"
- "Unable to save the server markers because the URL was nil"
- "does not exist"
- "exists"
- "kindList %@"

```
