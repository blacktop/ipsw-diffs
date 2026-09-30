## CoreUSDEdit

> `/System/Library/PrivateFrameworks/CoreUSDEdit.framework/Versions/A/CoreUSDEdit`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-28.0.8.0.0
-  __TEXT.__text: 0x14194ac
+28.40.2.0.0
+  __TEXT.__text: 0x14195e8
   __TEXT.__init_offsets: 0xc
   __TEXT.__objc_methlist: 0x948c
   __TEXT.__const: 0xe084f8
-  __TEXT.__gcc_except_tab: 0xeedb0
+  __TEXT.__gcc_except_tab: 0xeee04
   __TEXT.__oslogstring: 0x436c
   __TEXT.__cstring: 0x41722
   __TEXT.__ustring: 0xd08

   __DATA_CONST.__got: 0x16d0
   __AUTH_CONST.__const: 0x46380
   __AUTH_CONST.__cfstring: 0x8920
-  __AUTH_CONST.__objc_const: 0x1c0d8
+  __AUTH_CONST.__objc_const: 0x1c0f8
   __AUTH_CONST.__weak_auth_got: 0xfd0
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x40b8
+  __AUTH_CONST.__auth_got: 0x40c0
   __AUTH.__objc_data: 0x2ad0
   __AUTH.__data: 0xa50
   __AUTH.__thread_vars: 0x180
   __AUTH.__thread_data: 0x1
   __AUTH.__thread_bss: 0xd0
-  __DATA.__objc_ivar: 0x10d0
+  __DATA.__objc_ivar: 0x10d4
   __DATA.__data: 0x3c40
   __DATA.__common: 0x1418
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/usd/libusd_ms.dylib
   Functions: 43975
-  Symbols:   68746
+  Symbols:   68748
   CStrings:  9098
 
Symbols:
+ OBJC_IVAR_$_HdView._oneTouchPanYielded
+ _USDKitInitTypes
Functions:
~ -[HdView initWithFrame:device:renderer:] : 9596 -> 9612
~ -[HdView handleOneTouchPanGesture:] : 716 -> 868
~ -[ImageExportController writeToUrl:type:completionHandler:] : 5388 -> 5424
~ +[ImageExportController exportFromUsdDocument:renderer:] : 5776 -> 5792
~ -[USDExportController writeToUrl:expectedFinalURL:type:forSaveOperation:overrideFinalURL:error:] : 8828 -> 8880
~ -[MovieExportController writeToUrl:type:completionHandler:] : 7268 -> 7308
~ __ZN12HdAppleRTApp10initializeEv : 1332 -> 1336
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/usd/pxr/base/tf/iterator.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/usd/pxr/base/tf/notice.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/usd/pxr/base/tf/refPtr.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/usd/pxr/base/tf/weakPtrFacade.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/usd/pxr/base/vt/array.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/usd/pxr/base/vt/dictionary.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/usd/pxr/imaging/hd/sceneDelegate.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/usd/pxr/imaging/hd/timeSampleArray.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/usd/pxr/usd/sdf/declareHandles.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/usd/pxr/usd/sdf/listProxy.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/usd/pxr/usd/usd/object.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/usd/pxr/usd/usd/prim.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/usd/pxr/usd/usd/primData.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/usd/pxr/usd/usd/primRange.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/usd/pxr/usd/usd/stage.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/usd/pxr/usd/usdGeom/xformOp.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/usd/pxr/base/tf/iterator.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/usd/pxr/base/tf/notice.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/usd/pxr/base/tf/refPtr.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/usd/pxr/base/tf/weakPtrFacade.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/usd/pxr/base/vt/array.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/usd/pxr/base/vt/dictionary.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/usd/pxr/imaging/hd/sceneDelegate.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/usd/pxr/imaging/hd/timeSampleArray.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/usd/pxr/usd/sdf/declareHandles.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/usd/pxr/usd/sdf/listProxy.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/usd/pxr/usd/usd/object.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/usd/pxr/usd/usd/prim.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/usd/pxr/usd/usd/primData.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/usd/pxr/usd/usd/primRange.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/usd/pxr/usd/usd/stage.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/usd/pxr/usd/usdGeom/xformOp.h"
```
