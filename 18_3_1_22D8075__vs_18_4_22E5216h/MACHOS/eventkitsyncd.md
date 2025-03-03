## eventkitsyncd

> `/usr/libexec/eventkitsyncd`

```diff

-409.1.0.0.0
-  __TEXT.__text: 0x6d690
-  __TEXT.__auth_stubs: 0xd40
-  __TEXT.__objc_stubs: 0xc0e0
-  __TEXT.__objc_methlist: 0x6934
-  __TEXT.__cstring: 0x573b
-  __TEXT.__objc_methname: 0xee92
-  __TEXT.__objc_classname: 0x8db
-  __TEXT.__objc_methtype: 0x2321
-  __TEXT.__const: 0x288
-  __TEXT.__oslogstring: 0xa733
-  __TEXT.__gcc_except_tab: 0x8f0
-  __TEXT.__unwind_info: 0x1528
-  __DATA_CONST.__auth_got: 0x6b0
-  __DATA_CONST.__got: 0x418
-  __DATA_CONST.__const: 0x1740
+413.0.0.0.0
+  __TEXT.__text: 0x6dae0
+  __TEXT.__auth_stubs: 0xd10
+  __TEXT.__objc_stubs: 0xc180
+  __TEXT.__objc_methlist: 0x7008
+  __TEXT.__cstring: 0x5769
+  __TEXT.__objc_methname: 0xeedb
+  __TEXT.__objc_classname: 0x8e3
+  __TEXT.__objc_methtype: 0x2339
+  __TEXT.__const: 0x298
+  __TEXT.__oslogstring: 0xa844
+  __TEXT.__gcc_except_tab: 0x988
+  __TEXT.__unwind_info: 0x1550
+  __DATA_CONST.__auth_got: 0x698
+  __DATA_CONST.__got: 0x428
+  __DATA_CONST.__const: 0x1738
   __DATA_CONST.__cfstring: 0x4960
   __DATA_CONST.__objc_classlist: 0x2e8
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x260
+  __DATA_CONST.__objc_superrefs: 0x268
   __DATA_CONST.__objc_intobj: 0xd8
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_doubleobj: 0x50
-  __DATA.__objc_const: 0x10280
-  __DATA.__objc_selrefs: 0x3a98
-  __DATA.__objc_ivar: 0x910
+  __DATA.__objc_const: 0xf688
+  __DATA.__objc_selrefs: 0x3c88
+  __DATA.__objc_ivar: 0x914
   __DATA.__objc_data: 0x1d10
-  __DATA.__data: 0x7e8
+  __DATA.__data: 0x800
   __DATA.__bss: 0x188
   __DATA.__common: 0x1c
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2660
-  Symbols:   360
-  CStrings:  4634
+  Functions: 2672
+  Symbols:   359
+  CStrings:  4642
 
Symbols:
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSISO8601DateFormatter
- _fmod
- _objc_release_x10
- _objc_retain_x5
CStrings:
+ "== Started EventKitSync-413"
+ "@\"NSISO8601DateFormatter\""
+ "@40@0:8@16d24@32"
+ "Diagnostics syncReport dataWithContentsOfFile returned nil for path: %@"
+ "Ignoring diagnostic notification, feature flag disabled"
+ "NSError"
+ "Skipping notification, notifyForDriftOrDuplicates: [%{BOOL}d]"
+ "T@\"NSISO8601DateFormatter\",&,N,V_dateFormatter"
+ "Unable to open Calendar DB at path [%@] with error: [%@] - ignoring incomingData for drift or duplication with IDS identifier: %@"
+ "Unable to open Calendar DB at path [%@] with exception: [%@] - ignoring incomingData for drift or duplication with IDS identifier: %@"
+ "_createPhoneSackForWatchCache:andDatabase:"
+ "_dbFile"
+ "_forceDiagnosticForTesting"
+ "_minimumDateThresholdMet"
+ "driftResultsForCache:withDiagnosticTimestamp:andDatabase:"
+ "initWithDatabaseFile:"
+ "reason"
- "== Started EventKitSync-409.1"
- "@\"NSDateFormatter\""
- "Skipping notification, newDriftOrDuplicatesFound: [%{BOOL}d] sendDiagnosticNotificationEnabled: [%{BOOL}d]"
- "T@\"NSDateFormatter\",&,N,V_dateFormatter"
- "_createPhoneSackForWatchCache:"
- "_runDuplicateChecker"
- "_runOccurrenceCacheDumper"
- "driftResultsForCache:withDiagnosticTimestamp:"
- "yyyy-MM-dd HH:mm:ss ZZZZZ"

```
