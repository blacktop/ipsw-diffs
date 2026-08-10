## WatchControlSettings

> `/System/Library/PrivateFrameworks/WatchControlSettings.framework/WatchControlSettings`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__objc_ivar`
- `__DATA.__data`

```diff

-196.0.0.0.0
-  __TEXT.__text: 0x9ef4
+198.0.0.0.0
+  __TEXT.__text: 0x9fc4
   __TEXT.__objc_methlist: 0x874
-  __TEXT.__const: 0xc0
+  __TEXT.__const: 0xc8
   __TEXT.__cstring: 0x1901
   __TEXT.__gcc_except_tab: 0x54
-  __TEXT.__oslogstring: 0x606
+  __TEXT.__oslogstring: 0x6ea
   __TEXT.__dlopen_cstrs: 0x128
-  __TEXT.__unwind_info: 0x3b0
+  __TEXT.__unwind_info: 0x3b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 280
-  Symbols:   668
-  CStrings:  317
+  Symbols:   669
+  CStrings:  319
 
Symbols:
+ _AXAIWhiteGloveLoggingEnabled
Functions:
~ -[WatchControlSettings(Onboarding) setRequestToShowPracticeGrey:] : 352 -> 492
~ -[WCGesturesOverviewViewController_iOS _tryItOutOnAppleWatch] : 76 -> 144
CStrings:
+ "rdar://164150381 WCGesturesOverviewViewController_iOS _tryItOutOnAppleWatch tapped; requesting practice grey on watch"
+ "rdar://164150381 setRequestToShowPracticeGrey NPS write+sync issued value=%d domain=%{public}@ key=%{public}@"
```
