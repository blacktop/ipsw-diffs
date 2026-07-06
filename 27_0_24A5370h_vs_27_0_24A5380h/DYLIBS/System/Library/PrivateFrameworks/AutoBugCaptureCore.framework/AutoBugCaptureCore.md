## AutoBugCaptureCore

> `/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/AutoBugCaptureCore`

```diff

-  __TEXT.__text: 0x77a24
-  __TEXT.__objc_methlist: 0x5fac
-  __TEXT.__cstring: 0x51d5
+  __TEXT.__text: 0x77aec
+  __TEXT.__objc_methlist: 0x5fcc
+  __TEXT.__cstring: 0x51e1
   __TEXT.__const: 0x290
   __TEXT.__oslogstring: 0xf0b7
   __TEXT.__gcc_except_tab: 0xdd0
   __TEXT.__ustring: 0x8
   __TEXT.diag_actions: 0x5dcf
-  __TEXT.__unwind_info: 0x1578
+  __TEXT.__unwind_info: 0x15c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3728
+  __DATA_CONST.__objc_selrefs: 0x3740
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0x598
-  __DATA_CONST.__got: 0x4e8
+  __DATA_CONST.__got: 0x538
   __AUTH_CONST.__const: 0x620
   __AUTH_CONST.__cfstring: 0x6b40
-  __AUTH_CONST.__objc_const: 0xc8b0
+  __AUTH_CONST.__objc_const: 0xc8f0
   __AUTH_CONST.__objc_dictobj: 0x550
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_arrayobj: 0x3f0
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__auth_got: 0x830
   __AUTH.__objc_data: 0x8c0
-  __DATA.__objc_ivar: 0x690
-  __DATA.__data: 0xd28
+  __DATA.__objc_ivar: 0x698
+  __DATA.__data: 0xd30
   __DATA.__common: 0x18
-  __DATA.__bss: 0x110
+  __DATA.__bss: 0x108
   __DATA_DIRTY.__objc_data: 0xff0
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x288
+  __DATA_DIRTY.__bss: 0x290
   __DATA_DIRTY.__common: 0x1c
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2255
-  Symbols:   8185
-  CStrings:  3135
+  Functions: 2258
+  Symbols:   8197
+  CStrings:  3136
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[ABCPreferences _startObservingInstalledProfilesIfNeeded]
+ -[ABCPreferences _stopObservingInstalledProfiles]
+ -[ABCPreferences _tearDownCheckProfilesTimer]
+ _OBJC_IVAR_$_ABCPreferences._checkProfilesTimerLock
+ _OBJC_IVAR_$_ABCPreferences._installedProfilesObservationLock
+ _kNetDiagOptDiagsUseGMI
+ _objc_msgSend$_startObservingInstalledProfilesIfNeeded
+ _objc_msgSend$_stopObservingInstalledProfiles
+ _objc_msgSend$_tearDownCheckProfilesTimer
CStrings:
+ "diagsusegmi"

```
