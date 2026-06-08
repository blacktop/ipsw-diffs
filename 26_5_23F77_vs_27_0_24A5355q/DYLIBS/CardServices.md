## CardServices

> `/System/Library/PrivateFrameworks/CardServices.framework/CardServices`

```diff

 3520.8.1.0.0
-  __TEXT.__text: 0x2204
-  __TEXT.__auth_stubs: 0x350
+  __TEXT.__text: 0x200c
   __TEXT.__objc_methlist: 0x514
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x183
+  __TEXT.__cstring: 0x18c
   __TEXT.__oslogstring: 0x1f2
   __TEXT.__gcc_except_tab: 0x88
-  __TEXT.__unwind_info: 0x140
-  __TEXT.__objc_classname: 0x15b
-  __TEXT.__objc_methname: 0x810
-  __TEXT.__objc_methtype: 0x2e7
-  __TEXT.__objc_stubs: 0x520
-  __DATA_CONST.__got: 0x90
+  __TEXT.__unwind_info: 0x118
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1d0
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x50

   __DATA_CONST.__objc_selrefs: 0x2c8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x1b8
+  __DATA_CONST.__got: 0x90
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0xa0
   __AUTH_CONST.__objc_const: 0x1680
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x28
   __DATA.__data: 0x3c0

   - /System/Library/PrivateFrameworks/Cards.framework/Cards
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 48818508-EFF4-3588-AC2C-16C6A6AD0E8E
+  UUID: 94DA3CF5-0EFE-37CE-BB88-D5581740267B
   Functions: 65
-  Symbols:   425
-  CStrings:  212
+  Symbols:   427
+  CStrings:  28
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x26
Functions:
~ +[_CRSServiceBundleManager sharedInstance] : 176 -> 160
~ ___60-[_CRSServiceBundleManager getServiceBundlesWithCompletion:]_block_invoke : 212 -> 208
~ -[_CRSPassthroughService requestCard:reply:] : 148 -> 132
~ -[_CRSPassthroughService canSatisfyCardRequest:] : 72 -> 68
~ +[CRSIdentifiedServiceRegistry sharedInstance] : 176 -> 160
~ -[CRSIdentifiedServiceRegistry registerIdentifiedService:] : 204 -> 160
~ -[_CRSServiceBundle underlyingService] : 120 -> 116
~ -[_CRSServiceBundle _initializeServiceWithClass:] : 236 -> 196
~ -[_CRSServiceBundle serviceIdentifier] : 208 -> 192
~ -[CRSCardResponse request] : 16 -> 20
~ -[CRSCardResponse setRequest:] : 80 -> 20
~ -[CRSCardResponse card] : 16 -> 20
~ -[CRSCardResponse setCard:] : 80 -> 20
~ -[CRSCardRequest initWithContent:format:] : 224 -> 232
~ -[CRSCardRequest startWithReply:] : 428 -> 448
~ ___33-[CRSCardRequest startWithReply:]_block_invoke_2 : 864 -> 848
~ ___33-[CRSCardRequest startWithReply:]_block_invoke.52 : 172 -> 164
~ -[CRSCardRequest _loadAndRegisterBundleServices:] : 168 -> 164
~ ___49-[CRSCardRequest _loadAndRegisterBundleServices:]_block_invoke : 296 -> 248
~ ___49-[CRSCardRequest _loadAndRegisterBundleServices:]_block_invoke.63 : 352 -> 356
~ -[CRSCardRequest _tryRemainingCardServices:reply:] : 248 -> 256
~ ___50-[CRSCardRequest _tryRemainingCardServices:reply:]_block_invoke_2 : 380 -> 328
~ ___50-[CRSCardRequest _tryRemainingCardServices:reply:]_block_invoke.67 : 612 -> 604
~ -[CRSCardRequest content] : 16 -> 20
~ -[CRSCardRequest setContent:] : 80 -> 20
~ -[CRSCardRequest format] : 16 -> 20
~ -[CRSCardRequest setFormat:] : 16 -> 20
~ -[CRSCardRequest loadsBundleServices] : 16 -> 20
~ -[CRSCardRequest setLoadsBundleServices:] : 16 -> 20
~ -[CRSCardRequest _excludedServiceIdentifiers] : 16 -> 20
~ +[CRSCardRequest(Conveniences) registerService:] : 104 -> 100
~ -[_CRSCardServiceBundle underlyingService] : 120 -> 116
~ -[_CRSCardServiceBundle _initializeCardServiceWithClass:] : 236 -> 196
~ -[_CRSCardServiceBundle canSatisfyCardRequest:] : 120 -> 116
~ -[_CRSCardServiceBundle servicePriorityForRequest:] : 120 -> 116
~ ___50-[CRSCardRequest _tryRemainingCardServices:reply:]_block_invoke_2.cold.1 : 152 -> 108
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<CRCard>\""
- "@\"<CRContent>\""
- "@\"<CRContent>\"16@0:8"
- "@\"<CRSCardServing>\""
- "@\"<CRSServing>\""
- "@\"CRSCardRequest\""
- "@\"INInteraction\"16@0:8"
- "@\"NSArray\"16@0:8"
- "@\"NSMutableOrderedSet\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSSet\""
- "@\"NSSet\"16@0:8"
- "@\"NSString\"16@0:8"
- "@\"SFCard\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8:16@24"
- "@32@0:8@16Q24"
- "@40@0:8:16@24@32"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"<CRSCardRequesting>\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "CRCard"
- "CRContent"
- "CRSCardRequest"
- "CRSCardRequesting"
- "CRSCardResponse"
- "CRSCardServing"
- "CRSIdentifiedServiceRegistry"
- "CRSIdentifiedServing"
- "CRSRequest"
- "CRSResponse"
- "CRSServing"
- "Conveniences"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "Q24@0:8@\"<CRSCardRequesting>\"16"
- "Q24@0:8@16"
- "T#,R"
- "T@\"<CRCard>\",&,N,V_card"
- "T@\"<CRContent>\",&,N,V_content"
- "T@\"<CRContent>\",R,N"
- "T@\"CRSCardRequest\",&,N,V_request"
- "T@\"NSArray\",R,N"
- "T@\"NSSet\",C,N,G_excludedServiceIdentifiers,S_setExcludedServiceIdentifiers:,V_excludedServiceIdentifiers"
- "T@\"NSSet\",R,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"SFCard\",?,R,N"
- "TB,?,R,N"
- "TB,N,V_loadsBundleServices"
- "TB,R"
- "TQ,N,V_format"
- "TQ,R"
- "TQ,R,N"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_CRSCardServiceBundle"
- "_CRSCardServiceBundleManager"
- "_CRSPassthroughService"
- "_CRSServiceBundle"
- "_CRSServiceBundleManager"
- "_card"
- "_cardService"
- "_content"
- "_excludedServiceIdentifiers"
- "_format"
- "_identifiedServices"
- "_initializeCardServiceWithClass:"
- "_initializeServiceWithClass:"
- "_loadAndRegisterBundleServices:"
- "_loadsBundleServices"
- "_queue"
- "_request"
- "_service"
- "_setExcludedServiceIdentifiers:"
- "_tryRemainingCardServices:reply:"
- "addObject:"
- "allObjects"
- "array"
- "asynchronous"
- "autorelease"
- "backingCard"
- "bundleClass"
- "bundleDirectoryName"
- "bundleIdentifier"
- "canSatisfyCardRequest:"
- "card"
- "cardFormat"
- "cardIdentifier"
- "cardSections"
- "class"
- "compare:"
- "conformsToProtocol:"
- "containsObject:"
- "content"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "debugDescription"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "dismissalCommands"
- "encodeWithCoder:"
- "errorWithDomain:code:userInfo:"
- "excludedServiceIdentifiers"
- "filteredSetUsingPredicate:"
- "flexibleSectionOrder"
- "format"
- "getBundlesWithCompletion:"
- "getServiceBundlesWithCompletion:"
- "hash"
- "identifiedServices"
- "init"
- "initWithCoder:"
- "initWithContent:format:"
- "initialize"
- "interactions"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "lastObject"
- "loadCardWithCompletion:"
- "loadsBundleServices"
- "mutableCopy"
- "numberWithUnsignedInteger:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "predicateWithBlock:"
- "principalClass"
- "registerIdentifiedService:"
- "registerService:"
- "release"
- "removeLastObject"
- "request"
- "requestCard:reply:"
- "resolvedCardSections"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "reverseObjectEnumerator"
- "self"
- "serviceIdentifier"
- "servicePriorityForRequest:"
- "setCard:"
- "setContent:"
- "setFormat:"
- "setLoadsBundleServices:"
- "setRequest:"
- "sharedInstance"
- "sortUsingComparator:"
- "startWithReply:"
- "stringWithFormat:"
- "superclass"
- "supportsSecureCoding"
- "underlyingInteraction"
- "underlyingService"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8#16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"<CRCard>\">16"
- "v24@0:8Q16"
- "v32@0:8@\"<CRSCardRequesting>\"16@?<v@?@\"<CRCard>\"@\"NSError\">24"
- "v32@0:8@16@?24"
- "zone"

```
