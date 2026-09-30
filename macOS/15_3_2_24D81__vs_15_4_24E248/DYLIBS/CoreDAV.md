## CoreDAV

> `/System/Library/PrivateFrameworks/CoreDAV.framework/Versions/A/CoreDAV`

```diff

-1230.0.0.0.0
-  __TEXT.__text: 0x59ca0
+1230.5.1.0.0
+  __TEXT.__text: 0x5a638
   __TEXT.__auth_stubs: 0x730
-  __TEXT.__objc_methlist: 0x4e98
-  __TEXT.__cstring: 0x3c0e
+  __TEXT.__objc_methlist: 0x5768
+  __TEXT.__cstring: 0x3c76
   __TEXT.__const: 0xf0
   __TEXT.__oslogstring: 0x440b
-  __TEXT.__gcc_except_tab: 0x84c
-  __TEXT.__unwind_info: 0x1090
+  __TEXT.__gcc_except_tab: 0x820
+  __TEXT.__unwind_info: 0x10d8
   __TEXT.__objc_classname: 0xd8d
-  __TEXT.__objc_methname: 0xbc8e
+  __TEXT.__objc_methname: 0xbcae
   __TEXT.__objc_methtype: 0x1a7e
-  __TEXT.__objc_stubs: 0x7620
+  __TEXT.__objc_stubs: 0x7640
   __DATA_CONST.__got: 0x4a0
-  __DATA_CONST.__const: 0xab0
+  __DATA_CONST.__const: 0xac0
   __DATA_CONST.__objc_classlist: 0x380
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2648
+  __DATA_CONST.__objc_selrefs: 0x2798
   __DATA_CONST.__objc_superrefs: 0x360
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x3a8
   __AUTH_CONST.__const: 0x7d0
-  __AUTH_CONST.__cfstring: 0x5940
-  __AUTH_CONST.__objc_const: 0xbed8
+  __AUTH_CONST.__cfstring: 0x5960
+  __AUTH_CONST.__objc_const: 0xaef8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x79c

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 856559D0-450E-3F0F-9554-32D7CA03C7C2
-  Functions: 1691
-  Symbols:   4693
-  CStrings:  4066
+  UUID: DE82E350-1248-3462-A65C-E17A3DBAAEBB
+  Functions: 1747
+  Symbols:   4764
+  CStrings:  4070
 
Symbols:
+ +[CoreDAVItem parseRuleCache].cold.1
+ +[CoreDAVLogging sharedLogging].cold.1
+ +[CoreDAVRequestLogger _redactedHeadersFromHeaders:].cold.1
+ -[CoreDAVBulkChangeTask fillOutDataWithUUIDsToAddActions:hrefsToModDeleteActions:].cold.1
+ -[CoreDAVContainerSyncTaskGroup _bulkChange].cold.1
+ -[CoreDAVContainerSyncTaskGroup _bulkChange].cold.2
+ -[CoreDAVContainerSyncTaskGroup _bulkChange].cold.3
+ -[CoreDAVContainerSyncTaskGroup _getCTag].cold.1
+ -[CoreDAVContainerSyncTaskGroup _getDataPayloads].cold.1
+ -[CoreDAVContainerSyncTaskGroup _getDataPayloads].cold.2
+ -[CoreDAVContainerSyncTaskGroup _getETags].cold.1
+ -[CoreDAVContainerSyncTaskGroup _getOrder].cold.1
+ -[CoreDAVContainerSyncTaskGroup _pushActions].cold.1
+ -[CoreDAVContainerSyncTaskGroup _sendNextBatch].cold.1
+ -[CoreDAVDiscoveryTaskGroup completeDiscovery:error:].cold.1
+ -[CoreDAVDiscoveryTaskGroup completeDiscovery:error:].cold.2
+ -[CoreDAVDiscoveryTaskGroup completeDiscovery:error:].cold.3
+ -[CoreDAVDiscoveryTaskGroup completeDiscovery:error:].cold.4
+ -[CoreDAVRecursiveContainerSyncTaskGroup _getDataPayloads].cold.1
+ -[CoreDAVRecursiveContainerSyncTaskGroup _getDataPayloads].cold.2
+ -[CoreDAVRecursiveContainerSyncTaskGroup _getDataPayloads].cold.3
+ -[CoreDAVRecursiveContainerSyncTaskGroup _getItemTags].cold.1
+ -[CoreDAVRecursiveContainerSyncTaskGroup _getTask:finishedWithParsedContents:deletedItems:error:].cold.1
+ -[CoreDAVRecursiveContainerSyncTaskGroup _getTopFolderTags].cold.1
+ -[CoreDAVRecursiveContainerSyncTaskGroup _pushActions].cold.1
+ -[CoreDAVRecursiveContainerSyncTaskGroup initWithFolderURL:previousCTag:previousPTag:previousSyncToken:actions:syncItemOrder:context:accountInfoProvider:taskManager:].cold.1
+ -[CoreDAVRequestLogger logCoreDAVRequest:withTaskIdentifier:].cold.1
+ -[CoreDAVRequestLogger logCoreDAVResponseHeaders:andStatusCode:withTaskIdentifier:].cold.1
+ -[CoreDAVTask _session:dataTask:didReceiveData:].cold.1
+ -[CoreDAVTask _task:didFailWithError:].cold.1
+ -[CoreDAVTask _taskFinishedLoading:].cold.1
+ -[CoreDAVTask dealloc].cold.1
+ -[CoreDAVTask dealloc].cold.2
+ -[CoreDAVTask dealloc].cold.3
+ -[CoreDAVTask loadRequest:].cold.1
+ -[CoreDAVTask loadRequest:].cold.2
+ -[CoreDAVTask loadRequest:].cold.3
+ -[CoreDAVTask loadRequest:].cold.4
+ -[CoreDAVTask reset].cold.1
+ -[CoreDAVTaskGroup dealloc].cold.1
+ -[CoreDAVXMLData _prefixForNameSpace:].cold.1
+ -[CoreDAVXMLData appendElement:inNamespace:withStringContent:withAttributeNamesAndValues:].cold.1
+ -[CoreDAVXMLData appendElement:inNamespace:withStringContentAsCDATA:withAttributeNamesAndValues:].cold.1
+ -[CoreDAVXMLData appendElement:inNamespace:withStringContentAsCDATA:withAttributeNamesAndValues:].cold.2
+ -[CoreDAVXMLData endElement:inNamespace:].cold.1
+ -[CoreDAVXMLData endElement:inNamespace:].cold.2
+ -[CoreDAVXMLData endElement:inNamespace:].cold.3
+ -[CoreDAVXMLData startElement:inNamespace:withAttributeNamesAndValues:].cold.1
+ -[CoreDAVXMLData startElement:inNamespace:withAttributes:].cold.1
+ -[NSString(CoreDAVExtensions) CDVStringByAddingPercentEscapesForHREFIncludingPercent].cold.1
+ -[NSString(CoreDAVExtensions) CDVStringByAddingPercentEscapesForHREF].cold.1
+ -[NSString(CoreDAVExtensions) CDVStringByAddingPercentEscapesForUserOrPassword].cold.1
+ CDVAppleClientInfoString.cold.1
+ CDVRelativeOrderHeaderString.cold.1
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ __27-[CoreDAVTask loadRequest:]_block_invoke.103
+ __27-[CoreDAVTask loadRequest:]_block_invoke.110
+ __33-[CoreDAVTask performCoreDAVTask]_block_invoke.154
+ _objc_msgSend$base64EncodedStringWithOptions:
+ _systemVersionDict.cold.1
+ initializeLibXMLParser.cold.1
- __27-[CoreDAVTask loadRequest:]_block_invoke.102
- __27-[CoreDAVTask loadRequest:]_block_invoke.109
- __33-[CoreDAVTask performCoreDAVTask]_block_invoke.153
CStrings:
+ "/System/AppleInternal/Library/Frameworks/CalDAVServerSimulator.framework/CalDAVServerSimulator"
+ "Basic %@"
+ "base64EncodedStringWithOptions:"

```
