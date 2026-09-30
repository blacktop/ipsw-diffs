## NewsServices

> `/System/Library/PrivateFrameworks/NewsServices.framework/NewsServices`

```diff

-5805.0.0.0.0
-  __TEXT.__text: 0x2224
-  __TEXT.__auth_stubs: 0x310
+5861.1.0.0.0
+  __TEXT.__text: 0x2450
+  __TEXT.__auth_stubs: 0x2f0
   __TEXT.__objc_methlist: 0x464
   __TEXT.__const: 0x78
   __TEXT.__gcc_except_tab: 0x6c
   __TEXT.__cstring: 0x245
   __TEXT.__oslogstring: 0x1b
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__unwind_info: 0xf8
+  __TEXT.__unwind_info: 0x108
   __TEXT.__objc_classname: 0x117
   __TEXT.__objc_methname: 0xdfe
   __TEXT.__objc_methtype: 0x183

   __DATA_CONST.__objc_selrefs: 0x430
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x198
+  __AUTH_CONST.__auth_got: 0x188
   __AUTH_CONST.__cfstring: 0x260
   __AUTH_CONST.__objc_const: 0x8a0
   __AUTH.__objc_data: 0x230

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9F3C2CEE-5E22-3870-84D9-25BAEE42BEB7
-  Functions: 66
-  Symbols:   414
+  UUID: 0438D8E3-C8CD-3E1E-B95E-C4D3339B93B0
+  Functions: 67
+  Symbols:   412
   CStrings:  252
 
Symbols:
+ _objc_retain
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x3
- _objc_retain_x8
Functions:
+ sub_26754b0d8
~ -[NSSNewsViewController initWithArticleID:] : 164 -> 168
~ -[NSSNewsViewController initWithURL:] : 224 -> 228
~ -[NSSNewsViewController dealloc] : 220 -> 244
~ -[NSSNewsViewController viewDidLoad] : 440 -> 492
~ -[NSSNewsViewController viewDidLayoutSubviews] : 212 -> 228
~ -[NSSNewsViewController setLinkPreviewing:] : 236 -> 260
~ -[NSSNewsViewController requestRemoteViewController] : 580 -> 616
~ -[NSSNewsViewController setupRemoteViewController:] : 188 -> 204
~ -[NSSNewsViewController setRemoteViewContainerViewController:] : 20 -> 80
~ -[NSSNewsRemoteViewController dismissAnimated:] : 152 -> 164
~ -[NNCLastNewsStoryResult hash] : 160 -> 172
~ -[NNCLastNewsStoryResult isEqual:] : 548 -> 576
~ +[NNCComplicationDataSource staticTemplateForFamily:compact:] : 216 -> 228
~ +[NNCComplicationDataSource _oneLineHeadlineTextProviderForResult:] : 164 -> 184
~ +[NNCComplicationDataSource _templateForFamily:newsStoryResult:compact:] : 2692 -> 2832
~ +[NNCComplicationDataSource imageProviderWithForegroundName:compact:] : 252 -> 272
~ +[NNCComplicationDataSource fullColorImageProviderWithName:] : 540 -> 564

```
