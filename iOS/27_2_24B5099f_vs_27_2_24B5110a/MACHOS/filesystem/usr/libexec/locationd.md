## locationd

> `usr/libexec/locationd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3186.0.21.0.0
-  __TEXT.__text: 0x1af6148
+3186.0.22.0.0
+  __TEXT.__text: 0x1af6be4
   __TEXT.__auth_stubs: 0x6580
-  __TEXT.__objc_stubs: 0x3e8a0
-  __TEXT.__init_offsets: 0xc08
+  __TEXT.__objc_stubs: 0x3e8c0
+  __TEXT.__init_offsets: 0xc0c
   __TEXT.__objc_methlist: 0x2e9b8
-  __TEXT.__const: 0x166968
-  __TEXT.__gcc_except_tab: 0xdaafc
-  __TEXT.__oslogstring: 0x29356c
-  __TEXT.__cstring: 0x21129e
+  __TEXT.__const: 0x1669b8
+  __TEXT.__gcc_except_tab: 0xdaaf0
+  __TEXT.__oslogstring: 0x29376c
+  __TEXT.__cstring: 0x2115ae
   __TEXT.__objc_methname: 0x5d66f
   __TEXT.__objc_classname: 0x812d
   __TEXT.__objc_methtype: 0x39766

   __TEXT.__swift_as_cont: 0x1c
   __TEXT.__swift5_proto: 0x4c
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__unwind_info: 0x892c0
+  __TEXT.__unwind_info: 0x892f0
   __TEXT.__eh_frame: 0xf38
-  __DATA_CONST.__const: 0xc1d38
-  __DATA_CONST.__cfstring: 0x444e0
+  __DATA_CONST.__const: 0xc1d58
+  __DATA_CONST.__cfstring: 0x44760
   __DATA_CONST.__objc_classlist: 0x14d0
   __DATA_CONST.__objc_catlist: 0xc8
   __DATA_CONST.__objc_protolist: 0xe60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xae0
   __DATA_CONST.__objc_superrefs: 0x1328
-  __DATA_CONST.__objc_arraydata: 0x1bb0
+  __DATA_CONST.__objc_arraydata: 0x1c68
   __DATA_CONST.__objc_dictobj: 0xb18
   __DATA_CONST.__objc_intobj: 0x2e68
   __DATA_CONST.__objc_doubleobj: 0x160
-  __DATA_CONST.__objc_arrayobj: 0x978
+  __DATA_CONST.__objc_arrayobj: 0x9d8
   __DATA_CONST.__objc_floatobj: 0x80
   __DATA_CONST.__linkguard: 0x15
   __DATA_CONST.__auth_got: 0x32e0
-  __DATA_CONST.__got: 0x25e8
+  __DATA_CONST.__got: 0x25f0
   __DATA_CONST.__auth_ptr: 0x6a0
   __DATA.__objc_const: 0x4fc10
   __DATA.__objc_selrefs: 0x13c80

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 113631
-  Symbols:   2919
-  CStrings:  85400
+  Functions: 113642
+  Symbols:   2920
+  CStrings:  85426
 
Symbols:
+ _OBJC_CLASS_$_CLLocationCoordinate
CStrings:
+ "#Pinning Location unchanged (within range) and already authorized"
+ "#Pinning New Location has been preauthorized"
+ "#Pinning New Location received"
+ "#Pinning New location while already prompting for authorization."
+ "#Pinning Received a zero location!"
+ "#Pinning Received location is invalid. Let's have it dropped by next layers"
+ "/AppleInternal/Library/Frameworks/CoreAutomationDevice.framework"
+ "/AppleInternal/Library/LocationBundles/FenceTester.bundle"
+ "/AppleInternal/Library/LocationBundles/LocationMonitor.bundle"
+ "/System/Library/LocationBundles/SystemCustomization.bundle"
+ "/System/Library/LocationBundles/TimeZone.bundle"
+ "/System/Library/LocationBundles/WebBrowsingServices.bundle"
+ "/System/Library/PrivateFrameworks/HomeKitDaemon.framework"
+ "/System/Library/PrivateFrameworks/MobileWiFi.framework"
+ "HomeAccessory"
+ "com.apple.CalendarPebble"
+ "com.apple.Home"
+ "com.apple.Home.HomeWidgetTV"
+ "com.apple.MapKitTester"
+ "com.apple.PebbleSettingsApp"
+ "com.apple.WatchFacesWallpaperSupport.SnoopyPoster"
+ "com.apple.mobilesafari"
+ "com.apple.mobiletimer.WorldClocks"
+ "com.apple.reminders"
+ "com.apple.weather.nonPersonal"
+ "com.apple.weather.widget"
+ "{\"msg%{public}.0s\":\"#Pinning location changed, prompting for authorization\", \"previousLocation\":%{public, location:Encrypted_CLLocationCoordinate2D}.*P, \"newLocation\":%{public, location:Encrypted_CLLocationCoordinate2D}.*P}"
- "#Pinning Unsupported"
```
