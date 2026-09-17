## SiriAppLaunchSnippetProviderPlugin

> `/System/Library/FlowTools/SnippetService/ResponsePlugins/SiriAppLaunchSnippetProviderPlugin.bundle/Contents/MacOS/SiriAppLaunchSnippetProviderPlugin`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA.__objc_const`

```diff

-3600.8.6.0.0
-  __TEXT.__text: 0x4f58
-  __TEXT.__auth_stubs: 0x500
-  __TEXT.__cstring: 0x92
-  __TEXT.__const: 0x198
-  __TEXT.__swift5_typeref: 0x9e
-  __TEXT.__oslogstring: 0x21a
+3605.5.1.0.0
+  __TEXT.__text: 0x7768
+  __TEXT.__auth_stubs: 0x5c0
+  __TEXT.__cstring: 0x51
+  __TEXT.__const: 0x1d0
+  __TEXT.__swift5_typeref: 0xbc
+  __TEXT.__oslogstring: 0x3f8
   __TEXT.__objc_classname: 0x4d
   __TEXT.__constg_swiftt: 0x64
   __TEXT.__swift5_fieldmd: 0x20

   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0x198
-  __TEXT.__eh_frame: 0x1c0
+  __TEXT.__unwind_info: 0x218
+  __TEXT.__eh_frame: 0x278
   __DATA_CONST.__const: 0x118
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x280
-  __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__auth_ptr: 0xc0
+  __DATA_CONST.__auth_got: 0x2e0
+  __DATA_CONST.__got: 0xe8
+  __DATA_CONST.__auth_ptr: 0xd0
   __DATA.__objc_const: 0x90
-  __DATA.__data: 0xf0
-  __DATA.__common: 0x18
+  __DATA.__data: 0x118
+  __DATA.__common: 0x38
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/FlowToolsSnippetService.framework/Versions/A/FlowToolsSnippetService
   - /System/Library/PrivateFrameworks/IntelligenceFlow.framework/Versions/A/IntelligenceFlow

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 95
-  Symbols:   61
-  CStrings:  12
+  Functions: 127
+  Symbols:   63
+  CStrings:  16
 
Symbols:
+ _swift_arrayDestroy
+ _swift_bridgeObjectRelease_n
CStrings:
+ "AppLaunchResponseHandler deferring %ld apps in inform to per-entity rendering"
+ "AppLaunchResponseHandler registered for MarketplaceApplication handling"
+ "AppLaunchResponseHandler supports(): items=%ld apps=%ld in response type: %s"
+ "MarketplaceAppConverter missing required 'name' property"
+ "[MarketplaceAppConverter] 'iconURL' present but unreadable; shape=%{public}s"
+ "[MarketplaceAppConverter] entity carries neither 'iconURL' nor 'artwork'"
+ "[MarketplaceAppConverter] hydration check: nameLength=%{public}ld iconURLLength=%{public}ld genres=%{public}ld rating=%{bool,public}d reviewCount=%{bool,public}d bundleID=%{bool,public}d"
+ "[MarketplaceAppConverter] legacy artwork is neither string nor entity; shape=%{public}s"
+ "[MarketplaceAppConverter] propertyKeys=%{public}s iconShape=%{public}s"
+ "entityIdentifier"
+ "handle(item:context:) found MarketplaceApplication"
- "AppLaunchResponseHandler found %ld DisplayableMarketplaceApplication(s) in response type: %s"
- "AppLaunchResponseHandler registered for DisplayableMarketplaceApplication handling"
- "DisplayableMarketplaceApplication"
- "MarketplaceAppConverter missing 'result' entity"
- "MarketplaceAppConverter missing required 'name' property in result entity"
- "com.apple.siri.-MarketplaceIntents-AppIntents"
- "handle(item:context:) found DisplayableMarketplaceApplication for disambiguation"
```
