## NewsServices

> `/System/Library/PrivateFrameworks/NewsServices.framework/NewsServices`

```diff

-5883.0.0.0.0
-  __TEXT.__text: 0x2450
-  __TEXT.__auth_stubs: 0x2f0
+5916.1.0.0.0
+  __TEXT.__text: 0x21e8
   __TEXT.__objc_methlist: 0x464
   __TEXT.__const: 0x78
   __TEXT.__gcc_except_tab: 0x6c
-  __TEXT.__cstring: 0x245
+  __TEXT.__cstring: 0x249
   __TEXT.__oslogstring: 0x1b
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__unwind_info: 0x108
-  __TEXT.__objc_classname: 0x117
-  __TEXT.__objc_methname: 0xdfe
-  __TEXT.__objc_methtype: 0x183
-  __TEXT.__objc_stubs: 0xb20
-  __DATA_CONST.__got: 0x110
+  __TEXT.__unwind_info: 0x100
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xe8
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_selrefs: 0x430
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x188
+  __DATA_CONST.__got: 0x110
   __AUTH_CONST.__cfstring: 0x260
   __AUTH_CONST.__objc_const: 0x8a0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x230
   __DATA.__objc_ivar: 0x34
   __DATA.__data: 0x120

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CC85EFAC-E4E1-304A-AA07-E645AE3207FA
+  UUID: 642FDE0F-877B-3641-B1DE-624D30C63876
   Functions: 67
-  Symbols:   412
-  CStrings:  252
+  Symbols:   415
+  CStrings:  45
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x28
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_retain
Functions:
~ -[NSSNewsViewController initWithArticleID:] : 168 -> 164
~ -[NSSNewsViewController initWithArticleIDs:] : 152 -> 156
~ -[NSSNewsViewController initWithURL:] : 228 -> 224
~ -[NSSNewsViewController dealloc] : 244 -> 220
~ -[NSSNewsViewController viewDidLoad] : 492 -> 440
~ -[NSSNewsViewController viewDidLayoutSubviews] : 228 -> 212
~ -[NSSNewsViewController setLinkPreviewing:] : 260 -> 240
~ -[NSSNewsViewController requestRemoteViewController] : 616 -> 580
~ -[NSSNewsViewController setupRemoteViewController:] : 204 -> 188
~ -[NSSNewsViewController isLinkPreviewing] : 16 -> 20
~ -[NSSNewsViewController articleIDs] : 16 -> 20
~ -[NSSNewsViewController remoteViewContainerViewController] : 16 -> 20
~ -[NSSNewsViewController setRemoteViewContainerViewController:] : 80 -> 20
~ -[NSSNewsRemoteViewController dismissAnimated:] : 164 -> 152
~ -[NNCLastNewsStoryResult hash] : 172 -> 160
~ -[NNCLastNewsStoryResult isEqual:] : 576 -> 532
~ +[NNCComplicationDataSource staticTemplateForFamily:compact:] : 228 -> 216
~ +[NNCComplicationDataSource _oneLineHeadlineTextProviderForResult:] : 184 -> 164
~ +[NNCComplicationDataSource _templateForFamily:newsStoryResult:compact:] : 2832 -> 2620
~ +[NNCComplicationDataSource imageProviderWithForegroundName:compact:] : 272 -> 252
~ +[NNCComplicationDataSource fullColorImageProviderWithName:] : 564 -> 540
~ +[NNCComplicationDataSource _templateForFamily:newsStoryResult:compact:].cold.1 : 148 -> 104
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"_UIResilientRemoteViewContainerViewController\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@28@0:8@16B24"
- "@28@0:8q16B24"
- "@32@0:8:16@24"
- "@36@0:8q16@24B32"
- "@40@0:8:16@24@32"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NAVNewsArticleViewerRemoteProviderType"
- "NAVNewsArticleViewerServiceProviderType"
- "NNCComplicationDataSource"
- "NNCLastNewsStoryResult"
- "NSObject"
- "NSSArticle"
- "NSSArticleViewController"
- "NSSComplicationDataSource"
- "NSSNewsArticlePrefetcher"
- "NSSNewsRemoteViewController"
- "NSSNewsViewController"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"NSArray\",C,N,V_articleIDs"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_excerpt"
- "T@\"NSString\",C,N,V_headlineIdentifier"
- "T@\"NSString\",C,N,V_headlineTitle"
- "T@\"NSString\",C,N,V_sectionIdentifier"
- "T@\"NSString\",C,N,V_sectionName"
- "T@\"NSString\",C,N,V_sourceIdentifier"
- "T@\"NSString\",C,N,V_sourceName"
- "T@\"NSString\",R,C"
- "T@\"_UIResilientRemoteViewContainerViewController\",&,N,V_remoteViewContainerViewController"
- "TB,N,GisLinkPreviewing,V_linkPreviewing"
- "TQ,N,V_headlineIndex"
- "TQ,N,V_totalHeadlineCount"
- "TQ,R"
- "Tq,N,V_family"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_articleIDs"
- "_beginDelayingPresentation:cancellationHandler:"
- "_complicationTitle"
- "_endDelayingPresentation"
- "_excerpt"
- "_family"
- "_headlineIdentifier"
- "_headlineIndex"
- "_headlineTitle"
- "_linkPreviewing"
- "_loadingStoriesLargeString"
- "_loadingStoriesShortString"
- "_noNewStoriesLargeString"
- "_noNewStoriesShortString"
- "_oneLineHeadlineTextProviderForResult:"
- "_remoteViewContainerViewController"
- "_sectionIdentifier"
- "_sectionName"
- "_sourceIdentifier"
- "_sourceName"
- "_templateForFamily:newsStoryResult:compact:"
- "_totalHeadlineCount"
- "addChildViewController:"
- "addSubview:"
- "arrayWithObjects:count:"
- "articleIDs"
- "articleViewServiceProviderShouldLoadArticlesForArticleIDs:"
- "articleViewServiceProviderShouldPresentForLinkPreviewing:"
- "articleViewerRemoteProviderShouldDismissAnimated:"
- "autorelease"
- "bounds"
- "bundleForClass:"
- "canOpenURL:"
- "cancelPrefetchingArticlesForArticleIDs:"
- "class"
- "colorWithAlphaComponent:"
- "colorWithRed:green:blue:alpha:"
- "conformsToProtocol:"
- "dealloc"
- "debugDescription"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "didMoveToParentViewController:"
- "dismissAnimated:"
- "dismissViewControllerAnimated:completion:"
- "drawInRect:blendMode:alpha:"
- "excerpt"
- "exportedInterface"
- "extensionWithIdentifier:error:"
- "family"
- "fc_NewsArticleID"
- "fc_isNewsArticleURL"
- "fullColorImageProviderWithName:"
- "hash"
- "headlineIdentifier"
- "headlineIndex"
- "headlineTitle"
- "imageNamed:inBundle:compatibleWithTraitCollection:"
- "imageProviderWithForegroundName:compact:"
- "imageProviderWithOnePieceImage:"
- "imageWithActions:"
- "init"
- "initWithArticleID:"
- "initWithArticleIDs:"
- "initWithNibName:bundle:"
- "initWithSize:format:"
- "initWithURL:"
- "instantiateWithExtension:completion:"
- "interfaceWithProtocol:"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isLinkPreviewing"
- "isMemberOfClass:"
- "isProxy"
- "isViewLoaded"
- "linkPreviewing"
- "navigationController"
- "newsTintColor"
- "nss_newsComplicationTemplateForFamily:compact:"
- "parentViewController"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "popViewControllerAnimated:"
- "preferredFormat"
- "prefetchArticlesForArticleIDs:"
- "presentingViewController"
- "providerWithFullColorImage:monochromeFilterType:"
- "q"
- "q16@0:8"
- "release"
- "remoteViewContainerViewController"
- "remoteViewController"
- "removeFromParentViewController"
- "removeFromSuperview"
- "requestRemoteViewController"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "scale"
- "sectionIdentifier"
- "sectionName"
- "self"
- "serviceViewControllerInterface"
- "serviceViewControllerProxy"
- "setArticleIDs:"
- "setBackgroundColor:"
- "setBody1TextProvider:"
- "setBounds:"
- "setCircularTemplate:"
- "setExcerpt:"
- "setFamily:"
- "setFill"
- "setFrame:"
- "setHeaderImageProvider:"
- "setHeaderTextProvider:"
- "setHeadlineIdentifier:"
- "setHeadlineIndex:"
- "setHeadlineTitle:"
- "setImageProvider:"
- "setLinkPreviewing:"
- "setMetadata:"
- "setPreferredRange:"
- "setRemoteViewContainerViewController:"
- "setScale:"
- "setSectionIdentifier:"
- "setSectionName:"
- "setSourceIdentifier:"
- "setSourceName:"
- "setTextProvider:"
- "setTintColor:"
- "setTotalHeadlineCount:"
- "setupRemoteViewController:"
- "size"
- "sourceIdentifier"
- "sourceName"
- "staticTemplateForFamily:compact:"
- "stringWithFormat:"
- "superclass"
- "textProviderWithText:"
- "totalHeadlineCount"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v24@0:8q16"
- "view"
- "viewDidLayoutSubviews"
- "viewDidLoad"
- "viewServiceDidTerminateWithError:"
- "whiteColor"
- "willMoveToParentViewController:"
- "zone"

```
