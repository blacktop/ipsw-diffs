## SafariShared

> `/System/Library/PrivateFrameworks/SafariShared.framework/SafariShared`

```diff

-624.1.14.10.4
-  __TEXT.__text: 0x1af2d0
+624.1.16.10.6
+  __TEXT.__text: 0x1af5f0
   __TEXT.__auth_stubs: 0x2490
-  __TEXT.__objc_methlist: 0x1436c
+  __TEXT.__objc_methlist: 0x14374
   __TEXT.__const: 0x57ae0
-  __TEXT.__gcc_except_tab: 0x1e3c0
-  __TEXT.__cstring: 0x1ce25
+  __TEXT.__gcc_except_tab: 0x1e4a8
+  __TEXT.__cstring: 0x1ce85
   __TEXT.__ustring: 0xce62
   __TEXT.__oslogstring: 0x118e2
   __TEXT.__dlopen_cstrs: 0x25f

   __TEXT.__swift5_proto: 0xa0
   __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0xbab0
+  __TEXT.__unwind_info: 0xbb08
   __TEXT.__eh_frame: 0x80
   __TEXT.__objc_classname: 0x33eb
-  __TEXT.__objc_methname: 0x3acf8
-  __TEXT.__objc_methtype: 0xa75b
-  __TEXT.__objc_stubs: 0x1f800
+  __TEXT.__objc_methname: 0x3ad18
+  __TEXT.__objc_methtype: 0xa78b
+  __TEXT.__objc_stubs: 0x1f8a0
   __DATA_CONST.__got: 0x1638
-  __DATA_CONST.__const: 0x15448
+  __DATA_CONST.__const: 0x154e0
   __DATA_CONST.__objc_classlist: 0xb90
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x2b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb0c0
+  __DATA_CONST.__objc_selrefs: 0xb0c8
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x908
   __DATA_CONST.__objc_arraydata: 0xae0

   __AUTH_CONST.__objc_doubleobj: 0xa0
   __AUTH.__objc_data: 0x4658
   __AUTH.__data: 0x128
-  __DATA.__objc_ivar: 0x175c
+  __DATA.__objc_ivar: 0x1760
   __DATA.__data: 0x39b40
-  __DATA.__bss: 0x1290
+  __DATA.__bss: 0x12a0
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x2df0
   __DATA_DIRTY.__data: 0x10

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B4E7C6FC-E570-3618-9F05-361B7FD50246
-  Functions: 10239
-  Symbols:   34917
-  CStrings:  17404
+  UUID: C9041415-01D6-35E5-9DC2-90A1E8593E73
+  Functions: 10240
+  Symbols:   34938
+  CStrings:  17409
 
Symbols:
+ -[WBSHistoryItem updateLastVisit:]
+ -[WBSRecentWebSearchesController _effectiveRecentSearchEntries]
+ -[WBSRecentWebSearchesController _getRecentWebSearchEntries]
+ -[WBSRecentWebSearchesController initWithHistoryStore:defaultController:]
+ _OBJC_IVAR_$_WBSHistoryItem._lastVisit
+ _OBJC_IVAR_$_WBSRecentWebSearchesController._defaultController
+ __ZL28WBSHistoryItemLastVisitQueue
+ ___34-[WBSHistoryItem updateLastVisit:]_block_invoke
+ ___36-[WBSHistoryItem _addExistingVisit:]_block_invoke
+ ___36-[WBSHistoryItem mergeDataFromItem:]_block_invoke_2
+ ___60-[WBSHistoryItem(HistoryStreamedItem) updateLastVisitIfNil:]_block_invoke
+ ___72-[WBSHistoryItem removeVisitsOnSynchronizationQueue:candidateLastVisit:]_block_invoke
+ ___block_descriptor_40_e42_"WBSHistoryVisit"16?0"WBSHistoryVisit"8lu32l8
+ ___block_descriptor_40_ea8_32s_e42_"WBSHistoryVisit"16?0"WBSHistoryVisit"8ls32l8
+ ___block_descriptor_48_ea8_32s40s_e42_"WBSHistoryVisit"16?0"WBSHistoryVisit"8ls32l8s40l8
+ ___block_descriptor_64_ea8_32s40s48r56r_e5_v8?0lr48l8s32l8r56l8s40l8
+ _objc_msgSend$_effectiveRecentSearchEntries
+ _objc_msgSend$_getRecentWebSearchEntries
+ _objc_msgSend$clearRecentSearch:
+ _objc_msgSend$clearRecentSearches
+ _objc_msgSend$clearRecentSearchesAddedAfterDate:
+ _objc_msgSend$updateLastVisit:
- -[WBSHistoryItem lastVisitOnSynchronizationQueue]
- -[WBSHistoryItem lastVisitedTimeIntervalOnSynchronizationQueue]
- -[WBSRecentWebSearchesController initWithHistoryStore:]
- OBJC_IVAR_$_WBSHistoryItem._lastVisit
- ___23-[WBSHistoryItem title]_block_invoke
- ___37-[WBSHistoryItem lastVisitWasFailure]_block_invoke
- ___40-[WBSHistoryItem lastVisitWasHTTPNonGet]_block_invoke
- ___41-[WBSHistoryItem lastVisitedTimeInterval]_block_invoke
- ___50-[WBSHistoryItem lastVisitRedirectDestinationItem]_block_invoke
- _objc_msgSend$lastVisitOnSynchronizationQueue
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CKdGugBsgP_jr5L6somFFzRrQRXfw8dZifpkeIg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/wtf/HashTable.h"
+ "/AppleInternal/Library/BuildRoots/4~CKdGugBsgP_jr5L6somFFzRrQRXfw8dZifpkeIg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
+ "/AppleInternal/Library/BuildRoots/4~CKdGugBsgP_jr5L6somFFzRrQRXfw8dZifpkeIg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/wtf/Vector.h"
+ "8624.1.16.10.6"
+ "@\"WBSHistoryVisit\"16@?0@\"WBSHistoryVisit\"8"
+ "@\"WBSRecentWebSearchesController\""
+ "_defaultController"
+ "_effectiveRecentSearchEntries"
+ "_getRecentWebSearchEntries"
+ "com.apple.SafariShared.WBSHistoryItem.LastVisit"
+ "initWithHistoryStore:defaultController:"
+ "updateLastVisit:"
- "/AppleInternal/Library/BuildRoots/4~CJ8AugDAev2RH4Un7mfJYHqLgujOnAt4WnXhLHw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/wtf/HashTable.h"
- "/AppleInternal/Library/BuildRoots/4~CJ8AugDAev2RH4Un7mfJYHqLgujOnAt4WnXhLHw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
- "/AppleInternal/Library/BuildRoots/4~CJ8AugDAev2RH4Un7mfJYHqLgujOnAt4WnXhLHw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/wtf/Vector.h"
- "8624.1.14.10.4"
- "initWithHistoryStore:"
- "lastVisitOnSynchronizationQueue"
- "lastVisitedTimeIntervalOnSynchronizationQueue"

```
