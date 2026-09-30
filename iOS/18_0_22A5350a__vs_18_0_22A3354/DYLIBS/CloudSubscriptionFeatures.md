## CloudSubscriptionFeatures

> `/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures`

```diff

 301.22.0.29.0
-  __TEXT.__text: 0x8edd4
-  __TEXT.__auth_stubs: 0x1a00
-  __TEXT.__objc_methlist: 0x9fc
-  __TEXT.__const: 0x41c8
+  __TEXT.__text: 0x92168
+  __TEXT.__auth_stubs: 0x1a70
+  __TEXT.__objc_methlist: 0xa14
+  __TEXT.__const: 0x4218
   __TEXT.__gcc_except_tab: 0x80
-  __TEXT.__cstring: 0x3cc1
-  __TEXT.__oslogstring: 0x59ac
+  __TEXT.__cstring: 0x3fa1
+  __TEXT.__oslogstring: 0x5c6c
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__swift5_typeref: 0x160c
-  __TEXT.__swift5_fieldmd: 0x11bc
-  __TEXT.__constg_swiftt: 0x16c4
-  __TEXT.__swift5_reflstr: 0xcfd
+  __TEXT.__swift5_typeref: 0x163c
+  __TEXT.__swift5_fieldmd: 0x1208
+  __TEXT.__constg_swiftt: 0x1700
+  __TEXT.__swift5_reflstr: 0xd4d
   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_assocty: 0x240
-  __TEXT.__swift5_capture: 0x9e4
+  __TEXT.__swift5_capture: 0xa08
   __TEXT.__swift5_protos: 0x58
   __TEXT.__swift5_proto: 0x3a8
-  __TEXT.__swift5_types: 0x184
+  __TEXT.__swift5_types: 0x188
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x2468
-  __TEXT.__eh_frame: 0x4ec8
+  __TEXT.__unwind_info: 0x2518
+  __TEXT.__eh_frame: 0x50b0
   __TEXT.__objc_classname: 0xda
-  __TEXT.__objc_methname: 0x1973
+  __TEXT.__objc_methname: 0x1a16
   __TEXT.__objc_methtype: 0x250
   __TEXT.__objc_stubs: 0xa80
-  __DATA_CONST.__got: 0x428
+  __DATA_CONST.__got: 0x438
   __DATA_CONST.__const: 0x3b8
-  __DATA_CONST.__objc_classlist: 0x118
+  __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x790
+  __DATA_CONST.__objc_selrefs: 0x7b8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0xd10
-  __AUTH_CONST.__auth_ptr: 0x630
-  __AUTH_CONST.__const: 0x3f38
+  __AUTH_CONST.__auth_got: 0xd48
+  __AUTH_CONST.__auth_ptr: 0x5f8
+  __AUTH_CONST.__const: 0x3f88
   __AUTH_CONST.__cfstring: 0x400
-  __AUTH_CONST.__objc_const: 0x2ae0
+  __AUTH_CONST.__objc_const: 0x2bb8
   __AUTH.__objc_data: 0x158
   __DATA.__objc_ivar: 0x2c
-  __DATA.__data: 0xea0
+  __DATA.__data: 0xee0
   __DATA.__bss: 0x5010
-  __DATA.__common: 0x8
+  __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x1078
-  __DATA_DIRTY.__data: 0x17c8
+  __DATA_DIRTY.__data: 0x1898
   __DATA_DIRTY.__bss: 0x19c0
   __DATA_DIRTY.__common: 0x40
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2811
-  Symbols:   556
-  CStrings:  1187
+  Functions: 2849
+  Symbols:   558
+  CStrings:  1224
 
Symbols:
+ _OBJC_CLASS_$_LSApplicationRecord
CStrings:
+ "com.apple.CloudSubscriptionFeatures.datadetectors"
+ "App Installation for bundleIdentifier %!s(MISSING): %!{(MISSING)bool}d"
+ "_TtC25CloudSubscriptionFeatures18DataDetectorsCache"
+ "urlForRSVPDataDetectorsWithContext:"
+ "isRSVPFeatureAvailable()"
+ "com.apple.rsvp.dev"
+ "Invalid base URL"
+ "shouldShowRSVPDataDetectors()"
+ "CloudSubscriptionFeatures/DataDetectorsCache.swift"
+ "Updating DataDetectors cache with new shouldShowRSVPDataDetectors value %!{(MISSING)bool,public}d"
+ "rsvpDataDetectorsEnabled"
+ "All feature flags for rsvp are enabled, skipping XPCConnetion call"
+ "com.apple.rsvp.liveon"
+ "CloudSubscriptionFeatures/DaemonController+DataDetectors.swift"
+ "objectForKey:inDomain:"
+ "%!s(MISSING) feature: %!@(MISSING)"
+ "apps.rsvp.create-event"
+ "rsvp"
+ "Error fetching rsvp bag values %!s(MISSING)"
+ "Returning URL %!s(MISSING)"
+ "Unable to append context to URL, returning base URL %!s(MISSING)"
+ "shouldShowRSVPDataDetectors"
+ "setObject:forKey:inDomain:"
+ "initWithBundleIdentifier:allowPlaceholder:error:"
+ "https://icloud.com/events/new"
+ "Both runtime feature flags for rsvp are enabled, overriding setup bag values"
+ "%!s(MISSING) returning result: %!{(MISSING)bool,public}d"
+ "rsvpDataDetectors"
+ "com.apple.rsvp.qa"
+ "-timeSinceReference"
+ "DataDetectorsCache was passed invalid user defaults!"
+ "rsvpDefaultsKey"
+ "rsvpSubscriber"
+ "%!s(MISSING) requested"
+ "Runtime flag rsvpSubscriber is enabled, overriding feature check as true"
+ "setup bag results: rsvpEnabled=%!{(MISSING)bool,public}d, rsvpDataDetectorsEnabled=%!{(MISSING)bool,public}d"

```
