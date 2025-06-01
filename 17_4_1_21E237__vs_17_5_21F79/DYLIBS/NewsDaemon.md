## NewsDaemon

> `/System/Library/PrivateFrameworks/NewsDaemon.framework/NewsDaemon`

```diff

-5345.2.0.0.0
-  __TEXT.__text: 0x36d0
-  __TEXT.__auth_stubs: 0x330
-  __TEXT.__objc_methlist: 0x298
-  __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x743
-  __TEXT.__oslogstring: 0xec
-  __TEXT.__gcc_except_tab: 0x60
+5407.3.0.0.0
+  __TEXT.__text: 0x5c74
+  __TEXT.__auth_stubs: 0x380
+  __TEXT.__objc_methlist: 0x5b0
+  __TEXT.__const: 0x60
+  __TEXT.__cstring: 0x9a2
+  __TEXT.__gcc_except_tab: 0x8c
+  __TEXT.__oslogstring: 0x222
   __TEXT.__dlopen_cstrs: 0x48
-  __TEXT.__unwind_info: 0x14c
-  __TEXT.__objc_classname: 0xfe
-  __TEXT.__objc_methname: 0x986
-  __TEXT.__objc_methtype: 0x44e
-  __TEXT.__objc_stubs: 0x780
-  __DATA_CONST.__got: 0x20
-  __DATA_CONST.__const: 0x238
-  __DATA_CONST.__objc_classlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x48
+  __TEXT.__unwind_info: 0x20c
+  __TEXT.__objc_classname: 0x1a7
+  __TEXT.__objc_methname: 0x11a8
+  __TEXT.__objc_methtype: 0x5f5
+  __TEXT.__objc_stubs: 0xde0
+  __DATA_CONST.__got: 0x48
+  __DATA_CONST.__const: 0x2b8
+  __DATA_CONST.__objc_classlist: 0x50
+  __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xa90
-  __DATA_CONST.__objc_selrefs: 0x270
-  __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_classrefs: 0x90
-  __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x200
-  __AUTH_CONST.__objc_const: 0x1b0
-  __AUTH_CONST.__auth_got: 0x1a8
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x28
-  __DATA.__data: 0x360
-  __DATA.__bss: 0x28
-  __DATA_DIRTY.__objc_data: 0xa0
+  __DATA_CONST.__objc_const: 0x1058
+  __DATA_CONST.__objc_selrefs: 0x450
+  __DATA_CONST.__objc_protorefs: 0x38
+  __DATA_CONST.__objc_classrefs: 0xf0
+  __DATA_CONST.__objc_superrefs: 0x40
+  __AUTH_CONST.__cfstring: 0x3e0
+  __AUTH_CONST.__const: 0x40
+  __AUTH_CONST.__objc_const: 0x288
+  __AUTH_CONST.__auth_got: 0x1d0
+  __AUTH.__objc_data: 0x1e0
+  __DATA.__objc_ivar: 0x60
+  __DATA.__data: 0x480
+  __DATA.__bss: 0x40
+  __DATA_DIRTY.__const: 0x100
+  __DATA_DIRTY.__objc_const: 0x168
+  __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/NewsTransport.framework/NewsTransport
   - /System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/TeaFoundation.framework/TeaFoundation
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 76217546-4FEB-30CD-86B7-34E906C1A36E
-  Functions: 107
-  Symbols:   484
-  CStrings:  260
+  UUID: 47C5A5B2-81D6-3075-B6AD-1BEF6A79BAD1
+  Functions: 189
+  Symbols:   796
+  CStrings:  420
 
Symbols:
+ +[NDDownloadLimits defaultLimits]
+ +[NDDownloadLimits supportsSecureCoding]
+ +[NDTodayFeed supportsSecureCoding]
+ +[NDTodayFeedConfig supportsSecureCoding]
+ -[NDANFHelper _resourceIDFromURL:]
+ -[NDANFHelper _resourceIDsFromURLs:]
+ -[NDANFHelper manifestFromANFDocumentData:]
+ -[NDANFHelper popInterest]
+ -[NDANFHelper pushInterest]
+ -[NDANFHelperProxy .cxx_destruct]
+ -[NDANFHelperProxy _connectionToXPCService]
+ -[NDANFHelperProxy dealloc]
+ -[NDANFHelperProxy init]
+ -[NDANFHelperProxy manifestFromANFDocumentData:]
+ -[NDANFHelperProxy manifestFromANFDocumentData:reachedService:]
+ -[NDANFHelperProxy popInterest]
+ -[NDANFHelperProxy pushInterest]
+ -[NDANFHelperProxy setXpcConnection:]
+ -[NDANFHelperProxy setXpcConnectionInterest:]
+ -[NDANFHelperProxy setXpcConnectionLock:]
+ -[NDANFHelperProxy xpcConnectionInterest]
+ -[NDANFHelperProxy xpcConnectionLock]
+ -[NDANFHelperProxy xpcConnection]
+ -[NDANFHelperProxyWithFallback .cxx_destruct]
+ -[NDANFHelperProxyWithFallback inProcessHelper]
+ -[NDANFHelperProxyWithFallback init]
+ -[NDANFHelperProxyWithFallback manifestFromANFDocumentData:]
+ -[NDANFHelperProxyWithFallback popInterest]
+ -[NDANFHelperProxyWithFallback proxyHelper]
+ -[NDANFHelperProxyWithFallback pushInterest]
+ -[NDDownloadLimits copyWithZone:]
+ -[NDDownloadLimits description]
+ -[NDDownloadLimits encodeWithCoder:]
+ -[NDDownloadLimits hash]
+ -[NDDownloadLimits initWithCoder:]
+ -[NDDownloadLimits initWithMinDeviceStorage:maxDownloadStorage:]
+ -[NDDownloadLimits isEqual:]
+ -[NDDownloadLimits maxDownloadStorage]
+ -[NDDownloadLimits minDeviceStorage]
+ -[NDDownloadRequest articleID]
+ -[NDDownloadRequest issueID]
+ -[NDDownloadRequest puzzleID]
+ -[NDTodayFeed .cxx_destruct]
+ -[NDTodayFeed configData]
+ -[NDTodayFeed contentArchive]
+ -[NDTodayFeed contentManifest]
+ -[NDTodayFeed copyWithZone:]
+ -[NDTodayFeed description]
+ -[NDTodayFeed encodeWithCoder:]
+ -[NDTodayFeed initWithCoder:]
+ -[NDTodayFeed initWithConfigData:publishDate:contentManifest:contentArchive:]
+ -[NDTodayFeed publishDate]
+ -[NDTodayFeedConfig .cxx_destruct]
+ -[NDTodayFeedConfig copyWithZone:]
+ -[NDTodayFeedConfig description]
+ -[NDTodayFeedConfig encodeWithCoder:]
+ -[NDTodayFeedConfig initWithCoder:]
+ -[NDTodayFeedConfig initWithPublishDate:topStoriesArticleIDs:topStoriesPackageURLs:]
+ -[NDTodayFeedConfig publishDate]
+ -[NDTodayFeedConfig topStoriesArticleIDs]
+ -[NDTodayFeedConfig topStoriesPackageURLs]
+ _FCArticleIDPrefix
+ _FCDefaultLog
+ _FCIssueIDPrefix
+ _FCPuzzleIDPrefix
+ _NDANFDecodingServiceXPCConnection
+ _NDANFDecodingServiceXPCInterface
+ _NDArticleIDFromAudioContentID
+ _NDAudioContentIDFromArticleID
+ _NDAudioContentIDPrefix
+ _NDTodayFeedConfigDecodingServiceXPCConnection
+ _NDTodayFeedConfigDecodingServiceXPCConnection.onceToken
+ _NDTodayFeedConfigDecodingServiceXPCInterface
+ _NDTodayFeedMachServiceName
+ _NDTodayFeedServiceXPCConnection
+ _NDTodayFeedServiceXPCInterface
+ _OBJC_CLASS_$_FCANFDocumentManifest
+ _OBJC_CLASS_$_FCContentManifest
+ _OBJC_CLASS_$_NDANFHelper
+ _OBJC_CLASS_$_NDANFHelperProxy
+ _OBJC_CLASS_$_NDANFHelperProxyWithFallback
+ _OBJC_CLASS_$_NDDownloadLimits
+ _OBJC_CLASS_$_NDTodayFeed
+ _OBJC_CLASS_$_NDTodayFeedConfig
+ _OBJC_CLASS_$_NFUnfairLock
+ _OBJC_CLASS_$_NSByteCountFormatter
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_IVAR_$_NDANFHelperProxy._xpcConnection
+ _OBJC_IVAR_$_NDANFHelperProxy._xpcConnectionInterest
+ _OBJC_IVAR_$_NDANFHelperProxy._xpcConnectionLock
+ _OBJC_IVAR_$_NDANFHelperProxyWithFallback._inProcessHelper
+ _OBJC_IVAR_$_NDANFHelperProxyWithFallback._proxyHelper
+ _OBJC_IVAR_$_NDDownloadLimits._maxDownloadStorage
+ _OBJC_IVAR_$_NDDownloadLimits._minDeviceStorage
+ _OBJC_IVAR_$_NDTodayFeed._configData
+ _OBJC_IVAR_$_NDTodayFeed._contentArchive
+ _OBJC_IVAR_$_NDTodayFeed._contentManifest
+ _OBJC_IVAR_$_NDTodayFeed._publishDate
+ _OBJC_IVAR_$_NDTodayFeedConfig._publishDate
+ _OBJC_IVAR_$_NDTodayFeedConfig._topStoriesArticleIDs
+ _OBJC_IVAR_$_NDTodayFeedConfig._topStoriesPackageURLs
+ _OBJC_METACLASS_$_NDANFHelper
+ _OBJC_METACLASS_$_NDANFHelperProxy
+ _OBJC_METACLASS_$_NDANFHelperProxyWithFallback
+ _OBJC_METACLASS_$_NDDownloadLimits
+ _OBJC_METACLASS_$_NDTodayFeed
+ _OBJC_METACLASS_$_NDTodayFeedConfig
+ __OBJC_$_CLASS_METHODS_NDDownloadLimits
+ __OBJC_$_CLASS_METHODS_NDTodayFeed
+ __OBJC_$_CLASS_METHODS_NDTodayFeedConfig
+ __OBJC_$_CLASS_PROP_LIST_NDDownloadLimits
+ __OBJC_$_CLASS_PROP_LIST_NDTodayFeed
+ __OBJC_$_CLASS_PROP_LIST_NDTodayFeedConfig
+ __OBJC_$_INSTANCE_METHODS_NDANFHelper
+ __OBJC_$_INSTANCE_METHODS_NDANFHelperProxy
+ __OBJC_$_INSTANCE_METHODS_NDANFHelperProxyWithFallback
+ __OBJC_$_INSTANCE_METHODS_NDDownloadLimits
+ __OBJC_$_INSTANCE_METHODS_NDTodayFeed
+ __OBJC_$_INSTANCE_METHODS_NDTodayFeedConfig
+ __OBJC_$_INSTANCE_VARIABLES_NDANFHelperProxy
+ __OBJC_$_INSTANCE_VARIABLES_NDANFHelperProxyWithFallback
+ __OBJC_$_INSTANCE_VARIABLES_NDDownloadLimits
+ __OBJC_$_INSTANCE_VARIABLES_NDTodayFeed
+ __OBJC_$_INSTANCE_VARIABLES_NDTodayFeedConfig
+ __OBJC_$_PROP_LIST_NDANFHelperProxy
+ __OBJC_$_PROP_LIST_NDANFHelperProxyWithFallback
+ __OBJC_$_PROP_LIST_NDDownloadLimits
+ __OBJC_$_PROP_LIST_NDTodayFeed
+ __OBJC_$_PROP_LIST_NDTodayFeedConfig
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FCANFHelper
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NDANFDecodingServiceType
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NDTodayFeedConfigDecodingServiceType
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NDTodayFeedService
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FCANFHelper
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NDANFDecodingServiceType
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NDTodayFeedConfigDecodingServiceType
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NDTodayFeedService
+ __OBJC_$_PROTOCOL_REFS_NDTodayFeedService
+ __OBJC_CLASS_PROTOCOLS_$_NDANFHelper
+ __OBJC_CLASS_PROTOCOLS_$_NDANFHelperProxy
+ __OBJC_CLASS_PROTOCOLS_$_NDANFHelperProxyWithFallback
+ __OBJC_CLASS_PROTOCOLS_$_NDDownloadLimits
+ __OBJC_CLASS_PROTOCOLS_$_NDTodayFeed
+ __OBJC_CLASS_PROTOCOLS_$_NDTodayFeedConfig
+ __OBJC_CLASS_RO_$_NDANFHelper
+ __OBJC_CLASS_RO_$_NDANFHelperProxy
+ __OBJC_CLASS_RO_$_NDANFHelperProxyWithFallback
+ __OBJC_CLASS_RO_$_NDDownloadLimits
+ __OBJC_CLASS_RO_$_NDTodayFeed
+ __OBJC_CLASS_RO_$_NDTodayFeedConfig
+ __OBJC_LABEL_PROTOCOL_$_FCANFHelper
+ __OBJC_LABEL_PROTOCOL_$_NDANFDecodingServiceType
+ __OBJC_LABEL_PROTOCOL_$_NDTodayFeedConfigDecodingServiceType
+ __OBJC_LABEL_PROTOCOL_$_NDTodayFeedService
+ __OBJC_METACLASS_RO_$_NDANFHelper
+ __OBJC_METACLASS_RO_$_NDANFHelperProxy
+ __OBJC_METACLASS_RO_$_NDANFHelperProxyWithFallback
+ __OBJC_METACLASS_RO_$_NDDownloadLimits
+ __OBJC_METACLASS_RO_$_NDTodayFeed
+ __OBJC_METACLASS_RO_$_NDTodayFeedConfig
+ __OBJC_PROTOCOL_$_FCANFHelper
+ __OBJC_PROTOCOL_$_NDANFDecodingServiceType
+ __OBJC_PROTOCOL_$_NDTodayFeedConfigDecodingServiceType
+ __OBJC_PROTOCOL_$_NDTodayFeedService
+ __OBJC_PROTOCOL_REFERENCE_$_NDANFDecodingServiceType
+ __OBJC_PROTOCOL_REFERENCE_$_NDTodayFeedConfigDecodingServiceType
+ __OBJC_PROTOCOL_REFERENCE_$_NDTodayFeedService
+ ___33+[NDDownloadLimits defaultLimits]_block_invoke
+ ___36-[NDANFHelper _resourceIDsFromURLs:]_block_invoke
+ ___43-[NDANFHelperProxy _connectionToXPCService]_block_invoke
+ ___43-[NDANFHelperProxy _connectionToXPCService]_block_invoke.11
+ ___43-[NDANFHelperProxy _connectionToXPCService]_block_invoke.11.cold.1
+ ___43-[NDANFHelperProxy _connectionToXPCService]_block_invoke.cold.1
+ ___47-[NDDownloadRequest initWithContentID:options:]_block_invoke
+ ___47-[NDDownloadRequest initWithContentID:options:]_block_invoke.cold.1
+ ___63-[NDANFHelperProxy manifestFromANFDocumentData:reachedService:]_block_invoke
+ ___63-[NDANFHelperProxy manifestFromANFDocumentData:reachedService:]_block_invoke.5
+ ___63-[NDANFHelperProxy manifestFromANFDocumentData:reachedService:]_block_invoke.cold.1
+ ___63-[NDANFHelperProxy manifestFromANFDocumentData:reachedService:]_block_invoke_2
+ ___63-[NDANFHelperProxy manifestFromANFDocumentData:reachedService:]_block_invoke_2.cold.1
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___NDTodayFeedConfigDecodingServiceXPCConnection_block_invoke
+ ___NSArray0__struct
+ ___block_descriptor_40_e8_32s_e15_16?0"NSURL"8ls32l8
+ ___block_descriptor_40_e8_32s_e5_q8?0ls32l8
+ ___block_descriptor_56_e8_32s40r48r_e43_v24?0"FCANFDocumentManifest"8"NSError"16lr40l8s32l8r48l8
+ ___block_literal_global.10
+ ___block_literal_global.13
+ _defaultLimits.onceToken
+ _defaultLimits.s_defaults
+ _objc_enumerationMutation
+ _objc_msgSend$URL
+ _objc_msgSend$_connectionToXPCService
+ _objc_msgSend$_resourceIDFromURL:
+ _objc_msgSend$_resourceIDsFromURLs:
+ _objc_msgSend$activate
+ _objc_msgSend$allResourcesForImageIdentifier:
+ _objc_msgSend$array
+ _objc_msgSend$configData
+ _objc_msgSend$contentArchive
+ _objc_msgSend$contentManifest
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$data
+ _objc_msgSend$date
+ _objc_msgSend$decodeANFDocumentData:completion:
+ _objc_msgSend$decodeArrayOfObjectsOfClass:forKey:
+ _objc_msgSend$distantPast
+ _objc_msgSend$empty
+ _objc_msgSend$fc_millisecondTimeIntervalUntilNow
+ _objc_msgSend$fc_safelyAddObject:
+ _objc_msgSend$firstObject
+ _objc_msgSend$imageResourceForIdentifier:
+ _objc_msgSend$inProcessHelper
+ _objc_msgSend$initWithConfigData:publishDate:contentManifest:contentArchive:
+ _objc_msgSend$initWithMinDeviceStorage:maxDownloadStorage:
+ _objc_msgSend$initWithNonImageResourceIDs:optimalImageResourceIDs:smallestImageResourceIDs:
+ _objc_msgSend$initWithPublishDate:topStoriesArticleIDs:topStoriesPackageURLs:
+ _objc_msgSend$initWithServiceName:
+ _objc_msgSend$length
+ _objc_msgSend$lock
+ _objc_msgSend$manifestFromANFDocumentData:
+ _objc_msgSend$manifestFromANFDocumentData:reachedService:
+ _objc_msgSend$maxDownloadStorage
+ _objc_msgSend$minDeviceStorage
+ _objc_msgSend$numberWithLongLong:
+ _objc_msgSend$orderedImageIdentifiers
+ _objc_msgSend$popInterest
+ _objc_msgSend$proxyHelper
+ _objc_msgSend$publishDate
+ _objc_msgSend$pushInterest
+ _objc_msgSend$requiredNonImageResourceURLs
+ _objc_msgSend$setXpcConnection:
+ _objc_msgSend$setXpcConnectionInterest:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$stringFromByteCount:countStyle:
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$substringFromIndex:
+ _objc_msgSend$topStoriesArticleIDs
+ _objc_msgSend$topStoriesPackageURLs
+ _objc_msgSend$unlock
+ _objc_msgSend$unsignedLongLongValue
+ _objc_msgSend$xpcConnection
+ _objc_msgSend$xpcConnectionInterest
+ _objc_msgSend$xpcConnectionLock
+ _objc_release_x27
+ _objc_release_x28
+ _objc_release_x9
+ _xpc_add_bundle
- -[NDANFParsingService _requiredResourceURLsFromANFJSON:]
- -[NDANFParsingService resourceIDsFromFlintDocumentData:]
- _OBJC_CLASS_$_NDANFParsingService
- _OBJC_METACLASS_$_NDANFParsingService
- __OBJC_$_INSTANCE_METHODS_NDANFParsingService
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_FCFlintHelper
- __OBJC_$_PROTOCOL_METHOD_TYPES_FCFlintHelper
- __OBJC_CLASS_PROTOCOLS_$_NDANFParsingService
- __OBJC_CLASS_RO_$_NDANFParsingService
- __OBJC_LABEL_PROTOCOL_$_FCFlintHelper
- __OBJC_METACLASS_RO_$_NDANFParsingService
- __OBJC_PROTOCOL_$_FCFlintHelper
- ___56-[NDANFParsingService resourceIDsFromFlintDocumentData:]_block_invoke
- ___block_descriptor_32_e15_16?0"NSURL"8l
- _objc_msgSend$_requiredResourceURLsFromANFJSON:
- _objc_msgSend$requiredResourceURLs
CStrings:
+ "\x01\x11"
+ "\x04"
+ "-[NDDownloadRequest initWithContentID:options:]_block_invoke"
+ "/Library/Caches/com.apple.xbs/Sources/FeldsparServices/feldspar/Frameworks/NewsDaemon/Downloads/NDDownloadRequest.m"
+ "/System/Library/PrivateFrameworks/NewsUI2.framework/XPCServices/TodayFeedConfigDecoder.xpc"
+ "<%lu bytes>"
+ "@\"FCANFDocumentManifest\"24@0:8@\"NSData\"16"
+ "@\"FCContentArchive\""
+ "@\"FCContentManifest\""
+ "@\"NDANFHelper\""
+ "@\"NDANFHelperProxy\""
+ "@\"NFUnfairLock\""
+ "@\"NSArray\""
+ "@\"NSData\""
+ "@\"NSDate\""
+ "@32@0:8@16^B24"
+ "@32@0:8q16q24"
+ "@40@0:8@16@24@32"
+ "@48@0:8@16@24@32@40"
+ "ANFDecoder connection failed with error: %{public}@"
+ "ANFDecoder connection interrupted"
+ "ANFDecoder connection invalidated"
+ "ANFDecoder returned error: %{public}@"
+ "ANFDecoder returned manifest, time=%llums"
+ "ANFDecoder will invalidate connection due to zero interest"
+ "Audio"
+ "Decoded ANF in process"
+ "Decoded ANF via XPC Service"
+ "FCANFHelper"
+ "N"
+ "NDANFDecodingServiceType"
+ "NDANFHelper"
+ "NDANFHelperProxy"
+ "NDANFHelperProxyWithFallback"
+ "NDDownloadLimits"
+ "NDTodayFeed"
+ "NDTodayFeedConfig"
+ "NDTodayFeedConfigDecodingServiceType"
+ "NDTodayFeedService"
+ "Puzzle"
+ "T@\"FCContentArchive\",R,N,V_contentArchive"
+ "T@\"FCContentManifest\",R,N,V_contentManifest"
+ "T@\"NDANFHelper\",R,N,V_inProcessHelper"
+ "T@\"NDANFHelperProxy\",R,N,V_proxyHelper"
+ "T@\"NDDownloadLimits\",R,N"
+ "T@\"NFUnfairLock\",&,N,V_xpcConnectionLock"
+ "T@\"NSArray\",R,C,N,V_topStoriesArticleIDs"
+ "T@\"NSArray\",R,C,N,V_topStoriesPackageURLs"
+ "T@\"NSData\",R,N,V_configData"
+ "T@\"NSDate\",R,C,N,V_publishDate"
+ "T@\"NSDate\",R,N,V_publishDate"
+ "T@\"NSString\",R,C,N"
+ "T@\"NSXPCConnection\",&,N,V_xpcConnection"
+ "Tq,N,V_xpcConnectionInterest"
+ "Tq,R,N,V_maxDownloadStorage"
+ "Tq,R,N,V_minDeviceStorage"
+ "URL"
+ "_configData"
+ "_connectionToXPCService"
+ "_contentArchive"
+ "_contentManifest"
+ "_inProcessHelper"
+ "_maxDownloadStorage"
+ "_minDeviceStorage"
+ "_proxyHelper"
+ "_publishDate"
+ "_resourceIDFromURL:"
+ "_resourceIDsFromURLs:"
+ "_topStoriesArticleIDs"
+ "_topStoriesPackageURLs"
+ "_xpcConnection"
+ "_xpcConnectionInterest"
+ "_xpcConnectionLock"
+ "activate"
+ "adoptFeedConfigData:"
+ "allResourcesForImageIdentifier:"
+ "array"
+ "articleID"
+ "com.apple.news.ANFDecoder"
+ "com.apple.news.TodayFeedConfigDecoder"
+ "com.apple.newsd.today-feed"
+ "configData"
+ "contentArchive"
+ "contentManifest"
+ "countByEnumeratingWithState:objects:count:"
+ "data"
+ "decodeANFDocumentData:completion:"
+ "decodeArrayOfObjectsOfClass:forKey:"
+ "decodeTodayFeedConfigData:completion:"
+ "defaultLimits"
+ "distantPast"
+ "empty"
+ "fc_millisecondTimeIntervalUntilNow"
+ "fc_safelyAddObject:"
+ "fetchCachedTodayFeedWithCompletion:"
+ "firstObject"
+ "flushWithCompletion:"
+ "imageResourceForIdentifier:"
+ "inProcessHelper"
+ "initWithConfigData:publishDate:contentManifest:contentArchive:"
+ "initWithMinDeviceStorage:maxDownloadStorage:"
+ "initWithNonImageResourceIDs:optimalImageResourceIDs:smallestImageResourceIDs:"
+ "initWithPublishDate:topStoriesArticleIDs:topStoriesPackageURLs:"
+ "initWithServiceName:"
+ "issueID"
+ "length"
+ "lock"
+ "manifestFromANFDocumentData:"
+ "manifestFromANFDocumentData:reachedService:"
+ "maxDownloadStorage"
+ "minDeviceStorage"
+ "numberWithLongLong:"
+ "orderedImageIdentifiers"
+ "popInterest"
+ "proxyHelper"
+ "publishDate"
+ "pushInterest"
+ "puzzleID"
+ "q8@?0"
+ "requiredNonImageResourceURLs"
+ "setDownloadLimits:"
+ "setXpcConnection:"
+ "setXpcConnectionInterest:"
+ "setXpcConnectionLock:"
+ "stringByAppendingString:"
+ "stringFromByteCount:countStyle:"
+ "stringWithFormat:"
+ "substringFromIndex:"
+ "topStoriesArticleIDs"
+ "topStoriesPackageURLs"
+ "unknown content type for identifier: %@"
+ "unlock"
+ "unsignedLongLongValue"
+ "v24@0:8@\"NDDownloadLimits\"16"
+ "v24@0:8@\"NSData\"16"
+ "v24@0:8@?<v@?@\"NDTodayFeed\"@\"NSError\">16"
+ "v24@0:8q16"
+ "v24@?0@\"FCANFDocumentManifest\"8@\"NSError\"16"
+ "v32@0:8@\"NSData\"16@?<v@?@\"FCANFDocumentManifest\"@\"NSError\">24"
+ "v32@0:8@\"NSData\"16@?<v@?@\"NDTodayFeedConfig\"@\"NSError\">24"
+ "xpcConnection"
+ "xpcConnectionInterest"
+ "xpcConnectionLock"
- "@\"NSArray\"24@0:8@\"NSData\"16"
- "A"
- "FCFlintHelper"
- "NDANFParsingService"
- "_requiredResourceURLsFromANFJSON:"
- "requiredResourceURLs"
- "resourceIDsFromFlintDocumentData:"

```
