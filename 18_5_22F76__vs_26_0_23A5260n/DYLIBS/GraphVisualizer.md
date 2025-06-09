## GraphVisualizer

> `/System/Library/PrivateFrameworks/GraphVisualizer.framework/GraphVisualizer`

```diff

-220.1.0.0.0
-  __TEXT.__text: 0x8258
-  __TEXT.__auth_stubs: 0x170
-  __TEXT.__objc_methlist: 0x818
-  __TEXT.__cstring: 0x291
-  __TEXT.__const: 0x18
-  __TEXT.__gcc_except_tab: 0x24
-  __TEXT.__unwind_info: 0x218
-  __TEXT.__objc_classname: 0x66
-  __TEXT.__objc_methname: 0xc22
-  __TEXT.__objc_methtype: 0x285
-  __TEXT.__objc_stubs: 0x1140
-  __DATA_CONST.__got: 0x68
-  __DATA_CONST.__const: 0xb0
-  __DATA_CONST.__objc_classlist: 0x48
+307.0.0.0.0
+  __TEXT.__text: 0xa7a8
+  __TEXT.__auth_stubs: 0x290
+  __TEXT.__objc_methlist: 0xacc
+  __TEXT.__const: 0x30
+  __TEXT.__cstring: 0x2f2
+  __TEXT.__oslogstring: 0x21e
+  __TEXT.__gcc_except_tab: 0x34
+  __TEXT.__unwind_info: 0x2d0
+  __TEXT.__objc_classname: 0x78
+  __TEXT.__objc_methname: 0x1070
+  __TEXT.__objc_methtype: 0x36e
+  __TEXT.__objc_stubs: 0x16e0
+  __DATA_CONST.__got: 0x88
+  __DATA_CONST.__const: 0x1c0
+  __DATA_CONST.__objc_classlist: 0x50
+  __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x558
-  __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0xc8
+  __DATA_CONST.__objc_selrefs: 0x6c8
+  __DATA_CONST.__objc_superrefs: 0x48
+  __AUTH_CONST.__auth_got: 0x158
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0xe0
-  __AUTH_CONST.__objc_const: 0xb40
-  __DATA.__objc_ivar: 0x74
-  __DATA_DIRTY.__objc_data: 0x2d0
+  __AUTH_CONST.__cfstring: 0x260
+  __AUTH_CONST.__objc_const: 0xea0
+  __DATA.__objc_ivar: 0xa0
+  __DATA.__data: 0x60
+  __DATA.__bss: 0x20
+  __DATA_DIRTY.__objc_data: 0x320
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 37124162-32D3-3525-A01E-28103AA2744B
-  Functions: 195
-  Symbols:   666
-  CStrings:  296
+  UUID: 1E73C152-A966-3D3A-A39C-1BBD4E0DA912
+  Functions: 255
+  Symbols:   901
+  CStrings:  405
 
Symbols:
+ -[GVEdge initWithFromNode:to:reversed:]
+ -[GVEdge redundancyMax]
+ -[GVEdge redundancy]
+ -[GVEdge reverse]
+ -[GVEdge setRedundancy:]
+ -[GVEdge setRedundancyMax:]
+ -[GVEdge unreverse]
+ -[GVGraph _edges]
+ -[GVGraph _groups]
+ -[GVGraph _nodes]
+ -[GVGraph _sinkNodes]
+ -[GVGraph _sourceNodes]
+ -[GVGraph addEdgeFrom:to:reversed:].cold.1
+ -[GVGraph addEdgeFrom:to:reversed:].cold.2
+ -[GVGraph addNodeGroup:identifier:margins:]
+ -[GVGraph addNodeGroup:identifier:margins:].cold.1
+ -[GVGraph addNodeGroup:identifier:margins:].cold.2
+ -[GVGraph addNodeGroup:identifier:margins:].cold.3
+ -[GVGraph addNodeGroup:identifier:margins:].cold.4
+ -[GVGraph allowRedundantEdges]
+ -[GVGraph copyWithZone:]
+ -[GVGraph debugDescription]
+ -[GVGraph edgeCount]
+ -[GVGraph findEdgeBetween:and:]
+ -[GVGraph findEdgeFrom:to:]
+ -[GVGraph groups]
+ -[GVGraph hasEdgeBetween::]
+ -[GVGraph hasEdgeFrom:to:reversed:]
+ -[GVGraph inDegreeOf:]
+ -[GVGraph inEdgeCountOf:]
+ -[GVGraph inNodesOf:]
+ -[GVGraph minimizeEdgeCrossings]
+ -[GVGraph minimizeEdgeLengths]
+ -[GVGraph minimumSlack]
+ -[GVGraph nodeCount]
+ -[GVGraph outDegreeOf:]
+ -[GVGraph outEdgeCountOf:]
+ -[GVGraph outNodesOf:]
+ -[GVGraph randomSeed]
+ -[GVGraph removeEdge:]
+ -[GVGraph setAllowRedundantEdges:]
+ -[GVGraph setMinimizeEdgeCrossings:]
+ -[GVGraph setMinimizeEdgeLengths:]
+ -[GVGraph setRandomSeed:]
+ -[GVGraph set_edges:]
+ -[GVGraph set_groups:]
+ -[GVGraph set_nodes:]
+ -[GVGraph set_sinkNodes:]
+ -[GVGraph set_sourceNodes:]
+ -[GVGraph sinkNodes]
+ -[GVGraph slackOfEdge:]
+ -[GVGraph sourceNodes]
+ -[GVGraph traverseEdgesFromStart:callback:]
+ -[GVGraph traverseNodesFromStart:direction:randomize:callback:]
+ -[GVHorizontalRank breadth]
+ -[GVHorizontalRank initWithRank:separation:graph:]
+ -[GVHorizontalRank length]
+ -[GVIntegerMap allKeys]
+ -[GVIntegerMap countByEnumeratingWithState:objects:count:]
+ -[GVIntegerMap count]
+ -[GVIntegerMap dealloc]
+ -[GVIntegerMap debugDescription]
+ -[GVIntegerMap decrementValueForKey:]
+ -[GVIntegerMap incrementValueForKey:]
+ -[GVIntegerMap init]
+ -[GVIntegerMap integerForKey:]
+ -[GVIntegerMap objectForKeyedSubscript:]
+ -[GVIntegerMap removeObjectForKey:]
+ -[GVIntegerMap setInteger:forKey:]
+ -[GVIntegerMap setZeroForKey:]
+ -[GVLayout _locateCycles:visistedNodes:nodesInStack:reverseList:]
+ -[GVLayout buildRankObjectArray]
+ -[GVLayout clearNodeState]
+ -[GVLayout drawAllEdges:of:]
+ -[GVLayout drawAllGroups:of:]
+ -[GVLayout drawAllNodes:of:]
+ -[GVLayout graphOrig]
+ -[GVLayout graphPart]
+ -[GVLayout graphParts]
+ -[GVLayout insertDummiesBetweenRanks]
+ -[GVLayout packCut:]
+ -[GVLayout render:]
+ -[GVLayout setGraphOrig:]
+ -[GVLayout setGraphPart:]
+ -[GVLayout setGraphParts:]
+ -[GVLayout straighten]
+ -[GVNode setCenter:].cold.1
+ -[GVNode setCenter:].cold.2
+ -[GVNode setFrame:].cold.1
+ -[GVNode setFrame:].cold.2
+ -[GVNode setOrigin:].cold.1
+ -[GVNode setOrigin:].cold.2
+ -[GVRank breadth]
+ -[GVRank countByEnumeratingWithState:objects:count:]
+ -[GVRank count]
+ -[GVRank debugDescription]
+ -[GVRank graph]
+ -[GVRank initWithRank:separation:graph:]
+ -[GVRank length]
+ -[GVRank nextRank]
+ -[GVRank objectAtIndexedSubscript:]
+ -[GVRank prevRank]
+ -[GVRank rank]
+ -[GVRank reverseObjectEnumerator]
+ -[GVRank setGraph:]
+ -[GVRank setNextRank:]
+ -[GVRank setPrevRank:]
+ -[GVUIntegerMap allKeys]
+ -[GVUIntegerMap countByEnumeratingWithState:objects:count:]
+ -[GVUIntegerMap count]
+ -[GVUIntegerMap dealloc]
+ -[GVUIntegerMap debugDescription]
+ -[GVUIntegerMap decrementValueForKey:]
+ -[GVUIntegerMap incrementValueForKey:]
+ -[GVUIntegerMap init]
+ -[GVUIntegerMap integerForKey:]
+ -[GVUIntegerMap objectForKeyedSubscript:]
+ -[GVUIntegerMap removeObjectForKey:]
+ -[GVUIntegerMap setInteger:forKey:]
+ -[GVUIntegerMap setZeroForKey:]
+ -[GVVerticalRank breadth]
+ -[GVVerticalRank initWithRank:separation:graph:]
+ -[GVVerticalRank length]
+ GCC_except_table13
+ GCC_except_table27
+ GCC_except_table31
+ _CGPointZero
+ _CGRectInset
+ _CGRectIsEmpty
+ _CGRectNull
+ _CGRectUnion
+ _NSAllMapTableKeys
+ _OBJC_CLASS_$_GVIntegerMap
+ _OBJC_CLASS_$_GVUIntegerMap
+ _OBJC_CLASS_$_NSMapTable
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_IVAR_$_GVEdge.redundancy
+ _OBJC_IVAR_$_GVEdge.redundancyMax
+ _OBJC_IVAR_$_GVGraph._edges
+ _OBJC_IVAR_$_GVGraph._groups
+ _OBJC_IVAR_$_GVGraph._nodes
+ _OBJC_IVAR_$_GVGraph._sinkNodes
+ _OBJC_IVAR_$_GVGraph._sourceNodes
+ _OBJC_IVAR_$_GVGraph.allowRedundantEdges
+ _OBJC_IVAR_$_GVGraph.minimizeEdgeCrossings
+ _OBJC_IVAR_$_GVGraph.minimizeEdgeLengths
+ _OBJC_IVAR_$_GVGraph.randomSeed
+ _OBJC_IVAR_$_GVIntegerMap._map
+ _OBJC_IVAR_$_GVLayout.graphOrig
+ _OBJC_IVAR_$_GVLayout.graphPart
+ _OBJC_IVAR_$_GVLayout.graphParts
+ _OBJC_IVAR_$_GVRank.graph
+ _OBJC_IVAR_$_GVRank.nextRank
+ _OBJC_IVAR_$_GVRank.prevRank
+ _OBJC_IVAR_$_GVRank.rank
+ _OBJC_IVAR_$_GVUIntegerMap._map
+ _OBJC_METACLASS_$_GVIntegerMap
+ _OBJC_METACLASS_$_GVUIntegerMap
+ _OUTLINED_FUNCTION_0
+ __OBJC_$_INSTANCE_METHODS_GVIntegerMap
+ __OBJC_$_INSTANCE_METHODS_GVUIntegerMap
+ __OBJC_$_INSTANCE_VARIABLES_GVIntegerMap
+ __OBJC_$_INSTANCE_VARIABLES_GVUIntegerMap
+ __OBJC_$_PROP_LIST_GVIntegerMap
+ __OBJC_$_PROP_LIST_GVUIntegerMap
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_CLASS_PROTOCOLS_$_GVGraph
+ __OBJC_CLASS_RO_$_GVIntegerMap
+ __OBJC_CLASS_RO_$_GVUIntegerMap
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_METACLASS_RO_$_GVIntegerMap
+ __OBJC_METACLASS_RO_$_GVUIntegerMap
+ __OBJC_PROTOCOL_$_NSCopying
+ ___21-[GVRank sortByIndex]_block_invoke
+ ___22-[GVLayout straighten]_block_invoke
+ ___22-[GVLayout straighten]_block_invoke_2
+ ___24-[GVLayout removeCycles]_block_invoke
+ ___27-[GVGraph findEdgeFrom:to:]_block_invoke
+ ___31-[GVGraph findEdgeBetween:and:]_block_invoke
+ ___42-[GVLayout doLayout:direction:separation:]_block_invoke
+ ___44-[GVVerticalRank centerNodesWithRespectoTo:]_block_invoke
+ ___44-[GVVerticalRank centerNodesWithRespectoTo:]_block_invoke_2
+ ___44-[GVVerticalRank centerNodesWithRespectoTo:]_block_invoke_3
+ ___46-[GVHorizontalRank centerNodesWithRespectoTo:]_block_invoke
+ ___46-[GVHorizontalRank centerNodesWithRespectoTo:]_block_invoke_2
+ ___46-[GVHorizontalRank centerNodesWithRespectoTo:]_block_invoke_3
+ ___63-[GVGraph traverseNodesFromStart:direction:randomize:callback:]_block_invoke
+ ___NSArray0__struct
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_40_e16_q16?0"GVNode"8l
+ ___block_descriptor_40_e8_32b_e27_q24?0"GVNode"8"GVNode"16ls32l8
+ ___block_descriptor_40_e8_32b_e38_q32?0"GVEdge"8"GVNode"16"GVNode"24ls32l8
+ ___block_descriptor_40_e8_32o_e20_B24?0"GVNode"8^B16ls32l8
+ ___block_descriptor_40_e8_32o_e27_q24?0"GVNode"8"GVNode"16ls32l8
+ ___block_descriptor_40_e8_32o_e38_"NSMutableSet"32?0"GVNode"8^16^24ls32l8
+ ___block_descriptor_48_e8_32o40o_e38_q32?0"GVEdge"8"GVNode"16"GVNode"24ls32l8s40l8
+ ___block_descriptor_72_e8_32o40o48r_e38_q32?0"GVEdge"8"GVNode"16"GVNode"24ls32l8s40l8r48l8
+ ___block_literal_global.72
+ ___block_literal_global.74
+ ___block_literal_global.80
+ ___block_literal_global.82
+ ___gvgraph_logger_block_invoke
+ ___gvnode_logger_block_invoke
+ __os_log_error_impl
+ __os_log_impl
+ __traverse_edges
+ _dispatch_once
+ _gvgraph_logger.logger
+ _gvgraph_logger.onceToken
+ _gvnode_logger.logger
+ _gvnode_logger.onceToken
+ _malloc_type_calloc
+ _medianPt
+ _objc_autorelease
+ _objc_msgSend$_locateCycles:visistedNodes:nodesInStack:reverseList:
+ _objc_msgSend$allKeys
+ _objc_msgSend$allocWithZone:
+ _objc_msgSend$allowRedundantEdges
+ _objc_msgSend$breadth
+ _objc_msgSend$buildRankObjectArray
+ _objc_msgSend$clearNodeState
+ _objc_msgSend$debugDescription
+ _objc_msgSend$decrementValueForKey:
+ _objc_msgSend$drawAllEdges:of:
+ _objc_msgSend$drawAllGroups:of:
+ _objc_msgSend$drawAllNodes:of:
+ _objc_msgSend$drawGroup:frame:
+ _objc_msgSend$edgeCount
+ _objc_msgSend$findEdgeBetween:and:
+ _objc_msgSend$findEdgeFrom:to:
+ _objc_msgSend$frame
+ _objc_msgSend$graphPart
+ _objc_msgSend$graphParts
+ _objc_msgSend$groups
+ _objc_msgSend$hasEdgeBetween::
+ _objc_msgSend$hasEdgeFrom:to:reversed:
+ _objc_msgSend$inDegreeOf:
+ _objc_msgSend$inEdgeCountOf:
+ _objc_msgSend$inNodesOf:
+ _objc_msgSend$incrementValueForKey:
+ _objc_msgSend$init
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$initWithFromNode:to:reversed:
+ _objc_msgSend$initWithKeyOptions:valueOptions:capacity:
+ _objc_msgSend$initWithRank:separation:graph:
+ _objc_msgSend$insertDummiesBetweenRanks
+ _objc_msgSend$integerForKey:
+ _objc_msgSend$intersectsSet:
+ _objc_msgSend$isEqual:
+ _objc_msgSend$isEqualToSet:
+ _objc_msgSend$isSubsetOfSet:
+ _objc_msgSend$length
+ _objc_msgSend$minimizeEdgeCrossings
+ _objc_msgSend$minimizeEdgeLengths
+ _objc_msgSend$minimumSlack
+ _objc_msgSend$nextRank
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$objectsPassingTest:
+ _objc_msgSend$outDegreeOf:
+ _objc_msgSend$outNodesOf:
+ _objc_msgSend$packCut:
+ _objc_msgSend$prevRank
+ _objc_msgSend$ranks
+ _objc_msgSend$redundancy
+ _objc_msgSend$redundancyMax
+ _objc_msgSend$removeEdge:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$render:
+ _objc_msgSend$reverse
+ _objc_msgSend$setAllowRedundantEdges:
+ _objc_msgSend$setGraph:
+ _objc_msgSend$setGraphOrig:
+ _objc_msgSend$setGraphPart:
+ _objc_msgSend$setGraphParts:
+ _objc_msgSend$setInPriority:
+ _objc_msgSend$setInteger:forKey:
+ _objc_msgSend$setMinimizeEdgeCrossings:
+ _objc_msgSend$setMinimizeEdgeLengths:
+ _objc_msgSend$setNextRank:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setOutPriority:
+ _objc_msgSend$setPrevRank:
+ _objc_msgSend$setRandomSeed:
+ _objc_msgSend$setRanks:
+ _objc_msgSend$setRedundancy:
+ _objc_msgSend$setRedundancyMax:
+ _objc_msgSend$sinkNodes
+ _objc_msgSend$slackOfEdge:
+ _objc_msgSend$sortedArrayUsingComparator:
+ _objc_msgSend$sourceNodes
+ _objc_msgSend$straighten
+ _objc_msgSend$traverseEdgesFromStart:callback:
+ _objc_msgSend$traverseNodesFromStart:direction:randomize:callback:
+ _objc_msgSend$unreverse
+ _objc_opt_isKindOfClass
+ _objc_opt_new
+ _objc_release
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x25
+ _objc_retain
+ _objc_retain_x8
+ _os_log_create
+ _os_log_type_enabled
+ _rand_r
- +[GVInternalRenderer drawAllEdges:renderer:]
- +[GVInternalRenderer drawAllEdges:renderer:].cold.1
- +[GVInternalRenderer drawAllNodes:renderer:]
- +[GVInternalRenderer render:renderer:]
- -[GVDummyNode computePriority]
- -[GVEdge dealloc]
- -[GVEdge dummies]
- -[GVEdge init]
- -[GVEdge setDummies:]
- -[GVGraph edgeFrom:to:]
- -[GVGraph iterateOverAllEdges:]
- -[GVGraph iterateOverAllNodes:]
- -[GVGraph setEdges:]
- -[GVGraph setNodes:]
- -[GVGraph undoReverseEdge:]
- -[GVHorizontalRank height]
- -[GVHorizontalRank initWithSeparation:]
- -[GVHorizontalRank width]
- -[GVLayout _removeCycleDFS:visistedNodes:nodesInStack:]
- -[GVLayout buildRankIterators]
- -[GVLayout graph]
- -[GVLayout normalizeRanks]
- -[GVLayout packCutX:]
- -[GVLayout packCutY:]
- -[GVLayout removeSelfEdges]
- -[GVLayout selfEdges]
- -[GVLayout setGraph:]
- -[GVLayout setSelfEdges:]
- -[GVLayout straightenX]
- -[GVLayout straightenY]
- -[GVLayout undoRemoveSelfEdges]
- -[GVNode addEdgeFrom:]
- -[GVNode addEdgeTo:]
- -[GVNode computePriority]
- -[GVNode dealloc]
- -[GVNode hasEdgeFrom:]
- -[GVNode hasEdgeTo:]
- -[GVNode inDegree]
- -[GVNode inNodes]
- -[GVNode outDegree]
- -[GVNode outNodes]
- -[GVNode removeEdgeFrom:]
- -[GVNode removeEdgeTo:]
- -[GVNode setInNodes:]
- -[GVNode setOutNodes:]
- -[GVNode traversePostorder:withCallback:stopper:randomize:]
- -[GVNode traversePreorder:withCallback:randomize:]
- -[GVNode traversePreorder:withCallback:randomize:].cold.1
- -[GVRank height]
- -[GVRank inCrossings].cold.1
- -[GVRank initWithSeparation:]
- -[GVRank next]
- -[GVRank outCrossings].cold.1
- -[GVRank prev]
- -[GVRank setNext:]
- -[GVRank setPrev:]
- -[GVRank width]
- -[GVVerticalRank height]
- -[GVVerticalRank initWithSeparation:]
- -[GVVerticalRank width]
- GCC_except_table49
- GCC_except_table7
- OBJC_IVAR_$_GVNode.inNodes
- OBJC_IVAR_$_GVNode.outNodes
- _OBJC_CLASS_$_GVInternalRenderer
- _OBJC_IVAR_$_GVEdge.dummies
- _OBJC_IVAR_$_GVGraph.edges
- _OBJC_IVAR_$_GVGraph.nodes
- _OBJC_IVAR_$_GVLayout.graph
- _OBJC_IVAR_$_GVLayout.selfEdges
- _OBJC_IVAR_$_GVRank.next
- _OBJC_IVAR_$_GVRank.prev
- _OBJC_METACLASS_$_GVInternalRenderer
- __OBJC_$_CLASS_METHODS_GVInternalRenderer
- __OBJC_$_INSTANCE_METHODS_GVDummyNode
- __OBJC_CLASS_RO_$_GVInternalRenderer
- __OBJC_METACLASS_RO_$_GVInternalRenderer
- ___23-[GVGraph edgeFrom:to:]_block_invoke
- ___block_descriptor_40_e30_B32?0"GVNode"8"GVNode"16Q24l
- ___block_descriptor_64_e8_32o40r_e30_B32?0"GVNode"8"GVNode"16Q24ls32l8r40l8
- ___block_literal_global.150
- ___block_literal_global.152
- ___block_literal_global.154
- ___block_literal_global.156
- ___block_literal_global.49
- ___block_literal_global.56
- ___block_literal_global.59
- ___sortByDegree_block_invoke
- ___sortByInPriority_block_invoke
- ___sortByOutPriority_block_invoke
- __block_invoke
- __block_invoke_2
- __block_invoke_3
- __block_invoke_4
- __traverse_postorder
- __traverse_postorder.cold.1
- __traverse_postorder_randomized
- __traverse_postorder_randomized.cold.1
- __traverse_preorder
- __traverse_preorder.cold.1
- _arc4random
- _fisherYates
- _medianX
- _medianY
- _objc_msgSend$_removeCycleDFS:visistedNodes:nodesInStack:
- _objc_msgSend$addEdgeTo:
- _objc_msgSend$buildRankIterators
- _objc_msgSend$computePriority
- _objc_msgSend$drawAllEdges:renderer:
- _objc_msgSend$drawAllNodes:renderer:
- _objc_msgSend$dummies
- _objc_msgSend$edgeFrom:to:
- _objc_msgSend$hasEdgeFrom:
- _objc_msgSend$hasEdgeFrom:to:
- _objc_msgSend$hasEdgeTo:
- _objc_msgSend$height
- _objc_msgSend$inDegree
- _objc_msgSend$inNodes
- _objc_msgSend$initWithSeparation:
- _objc_msgSend$layoutGraph:withDirection:separation:
- _objc_msgSend$minusSet:
- _objc_msgSend$nextObject
- _objc_msgSend$normalizeRanks
- _objc_msgSend$orderedSet
- _objc_msgSend$outDegree
- _objc_msgSend$outNodes
- _objc_msgSend$packCutX:
- _objc_msgSend$packCutY:
- _objc_msgSend$removeEdgeFrom:to:
- _objc_msgSend$removeEdgeTo:
- _objc_msgSend$removeNode:
- _objc_msgSend$removeSelfEdges
- _objc_msgSend$render:renderer:
- _objc_msgSend$setWithObject:
- _objc_msgSend$size
- _objc_msgSend$straightenX
- _objc_msgSend$straightenY
- _objc_msgSend$string
- _objc_msgSend$traversePreorder:withCallback:randomize:
- _objc_msgSend$undoReverseEdge:
- _objc_msgSend$unionOrderedSet:
- _objc_msgSend$width
- _objc_release_x27
- _object_getClassName
CStrings:
+ "\n  "
+ "\n  Edges:\n\n"
+ "\n  Nodes:\n\n"
+ "  "
+ "  ["
+ " Sink"
+ " Solo"
+ " Source"
+ " center=(%.2f,%.2f)"
+ " index=%lu"
+ " rank=%lu"
+ "%@\n  %ld: %@"
+ "%@ [%p %s %p]"
+ "%@ nodeCount=%lu edgeCount=%lu"
+ "%@ rank:%ld"
+ "%@ size=(%.2f,%.2f)%@"
+ "%{public}s A unique identifier is required when adding a GVNodeGroup."
+ "%{public}s Adding a GVNodeGroup with contents that overlap with an existing group is unsupported."
+ "%{public}s Adding a GVNodeGroup with the same contents as an existing group has no effect."
+ "%{public}s center property is read-only."
+ "%{public}s frame property is read-only."
+ "%{public}s origin property is read-only."
+ "->"
+ "-[GVGraph addEdgeFrom:to:] Edge from GVNode %p to GVNode %p already exists."
+ "-[GVGraph addEdgeFrom:to:] Edge from GVNode %p to itself is not currently supported."
+ "-[GVGraph addNodeGroup:identifier:margins:]"
+ "-[GVNode setCenter:]"
+ "-[GVNode setFrame:]"
+ "-[GVNode setOrigin:]"
+ "<-"
+ "@\"NSMapTable\""
+ "@\"NSMutableDictionary\""
+ "@\"NSMutableSet\"32@?0@\"GVNode\"8^@16^@24"
+ "@24@0:8Q16"
+ "@24@0:8^{_NSZone=}16"
+ "@36@0:8@16@24B32"
+ "@48@0:8q16{CGSize=dd}24@40"
+ "B24@?0@\"GVNode\"8^B16"
+ "B36@0:8@16@24B32"
+ "GVIntegerMap"
+ "GVRank.m"
+ "GVUIntegerMap"
+ "I"
+ "I16@0:8"
+ "NSCopying"
+ "Q24@0:8@16"
+ "Q40@0:8^{?=Q^@^Q[5Q]}16^@24Q32"
+ "T@\"GVGraph\",&,N,VgraphOrig"
+ "T@\"GVGraph\",&,N,VgraphPart"
+ "T@\"GVGraph\",Vgraph"
+ "T@\"GVNode\",W,N,Vnext"
+ "T@\"GVNode\",W,N,Vprev"
+ "T@\"GVRank\",W,N,VnextRank"
+ "T@\"GVRank\",W,N,VprevRank"
+ "T@\"NSArray\",R,C"
+ "T@\"NSDictionary\",R,N"
+ "T@\"NSMutableArray\",&,N,VgraphParts"
+ "T@\"NSMutableDictionary\",&,N,V_groups"
+ "T@\"NSMutableOrderedSet\",&,N,V_edges"
+ "T@\"NSMutableOrderedSet\",&,N,V_nodes"
+ "T@\"NSMutableOrderedSet\",&,N,V_sinkNodes"
+ "T@\"NSMutableOrderedSet\",&,N,V_sourceNodes"
+ "T@\"NSOrderedSet\",R,N"
+ "TB,N,VallowRedundantEdges"
+ "TB,N,VminimizeEdgeCrossings"
+ "TB,N,VminimizeEdgeLengths"
+ "TI,N,VrandomSeed"
+ "TI,N,Vredundancy"
+ "TI,N,VredundancyMax"
+ "TQ,R,N"
+ "Tq,R,Vrank"
+ "T{CGPoint=dd},R,N"
+ "]\n"
+ "_edges"
+ "_groups"
+ "_locateCycles:visistedNodes:nodesInStack:reverseList:"
+ "_map"
+ "_nodes"
+ "_sinkNodes"
+ "_sourceNodes"
+ "addNodeGroup:identifier:margins:"
+ "allKeys"
+ "allocWithZone:"
+ "allowRedundantEdges"
+ "breadth"
+ "buildRankObjectArray"
+ "clearNodeState"
+ "com.apple.graphvisualizer"
+ "copyWithZone:"
+ "debugDescription"
+ "decrementValueForKey:"
+ "drawAllEdges:of:"
+ "drawAllGroups:of:"
+ "drawAllNodes:of:"
+ "drawGroup:frame:"
+ "edgeCount"
+ "findEdgeBetween:and:"
+ "findEdgeFrom:to:"
+ "graphOrig"
+ "graphPart"
+ "graphParts"
+ "groups"
+ "hasEdgeBetween::"
+ "hasEdgeFrom:to:reversed:"
+ "inDegreeOf:"
+ "inEdgeCountOf:"
+ "inNodesOf:"
+ "incrementValueForKey:"
+ "initWithCapacity:"
+ "initWithFromNode:to:reversed:"
+ "initWithKeyOptions:valueOptions:capacity:"
+ "initWithRank:separation:graph:"
+ "insertDummiesBetweenRanks"
+ "integerForKey:"
+ "intersectsSet:"
+ "isEqual:"
+ "isEqualToSet:"
+ "isSubsetOfSet:"
+ "length"
+ "minimizeEdgeCrossings"
+ "minimizeEdgeLengths"
+ "minimumSlack"
+ "nextRank"
+ "nodeCount"
+ "numberWithInteger:"
+ "numberWithUnsignedInteger:"
+ "objectForKey:"
+ "objectForKeyedSubscript:"
+ "objectsPassingTest:"
+ "outDegreeOf:"
+ "outEdgeCountOf:"
+ "outNodesOf:"
+ "packCut:"
+ "prevRank"
+ "q16@?0@\"GVNode\"8"
+ "q24@0:8@16"
+ "q32@?0@\"GVEdge\"8@\"GVNode\"16@\"GVNode\"24"
+ "randomSeed"
+ "rank == prevRank || rank == nextRank"
+ "redundancy"
+ "redundancyMax"
+ "removeEdge:"
+ "removeObjectForKey:"
+ "reverse"
+ "setAllowRedundantEdges:"
+ "setGraphOrig:"
+ "setGraphPart:"
+ "setGraphParts:"
+ "setInteger:forKey:"
+ "setMinimizeEdgeCrossings:"
+ "setMinimizeEdgeLengths:"
+ "setNextRank:"
+ "setObject:forKey:"
+ "setPrevRank:"
+ "setRandomSeed:"
+ "setRedundancy:"
+ "setRedundancyMax:"
+ "setZeroForKey:"
+ "set_edges:"
+ "set_groups:"
+ "set_nodes:"
+ "set_sinkNodes:"
+ "set_sourceNodes:"
+ "sinkNodes"
+ "slackOfEdge:"
+ "sortedArrayUsingComparator:"
+ "sourceNodes"
+ "straighten"
+ "traverseEdgesFromStart:callback:"
+ "traverseNodesFromStart:direction:randomize:callback:"
+ "unreverse"
+ "v20@0:8I16"
+ "v32@0:8@16@?24"
+ "v32@0:8Q16@24"
+ "v32@0:8q16@24"
+ "v40@0:8@16i24B28@?32"
+ "v40@0:8@16{CGPoint=dd}24"
+ "v48@0:8@16@24@32@40"
+ "v64@0:8@16@24{?=dddd}32"
+ "v8@?0"
- "\nEdges:\n\n"
- "\nNodes:\n\n"
- " (r)"
- "%p [%p -> %p%@]"
- "%p [%s center=<%f,%f>]"
- "+[GVInternalRenderer drawAllEdges:renderer:]"
- "-[GVRank inCrossings]"
- "-[GVRank outCrossings]"
- "0 && \"unreachable\""
- "@32@0:8{CGSize=dd}16"
- "B32@?0@\"GVNode\"8@\"GVNode\"16Q24"
- "GVInternalRenderer"
- "GVNode.m"
- "GVRenderer.m"
- "T@\"GVGraph\",N,Vgraph"
- "T@\"GVNode\",N,Vnext"
- "T@\"GVNode\",N,Vprev"
- "T@\"GVRank\",N,Vnext"
- "T@\"GVRank\",N,Vprev"
- "T@\"NSMutableArray\",&,N,Vdummies"
- "T@\"NSMutableArray\",&,N,VselfEdges"
- "T@\"NSMutableOrderedSet\",&,N,Vedges"
- "T@\"NSMutableOrderedSet\",&,N,VinNodes"
- "T@\"NSMutableOrderedSet\",&,N,Vnodes"
- "T@\"NSMutableOrderedSet\",&,N,VoutNodes"
- "T{CGPoint=dd},N"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N"
- "_removeCycleDFS:visistedNodes:nodesInStack:"
- "_traverse_postorder"
- "_traverse_postorder_randomized"
- "_traverse_preorder"
- "_traverse_preorder_randomized"
- "addEdgeFrom:"
- "addEdgeTo:"
- "buildRankIterators"
- "computePriority"
- "drawAllEdges:renderer:"
- "drawAllNodes:renderer:"
- "dummies"
- "edgeFrom:to:"
- "hasEdgeFrom:"
- "hasEdgeTo:"
- "height"
- "inDegree"
- "inNodeI.rank == inNodeJ.rank"
- "inNodes"
- "initWithSeparation:"
- "iterateOverAllEdges:"
- "iterateOverAllNodes:"
- "minusSet:"
- "nextObject"
- "normalizeRanks"
- "orderedSet"
- "outDegree"
- "outNodeI.rank == outNodeJ.rank"
- "outNodes"
- "packCutX:"
- "packCutY:"
- "rank == prev || rank == next"
- "removeEdgeFrom:"
- "removeEdgeTo:"
- "removeSelfEdges"
- "render:renderer:"
- "selfEdges"
- "setDummies:"
- "setEdges:"
- "setInNodes:"
- "setNodes:"
- "setOutNodes:"
- "setSelfEdges:"
- "setWithObject:"
- "straightenX"
- "straightenY"
- "string"
- "traversePostorder:withCallback:stopper:randomize:"
- "traversePreorder:withCallback:randomize:"
- "undoRemoveSelfEdges"
- "undoReverseEdge:"
- "unionOrderedSet:"
- "v24@0:8@?16"
- "v32@0:8@16d24"
- "v32@0:8i16@?20B28"
- "v40@0:8@16@24@32"
- "v40@0:8i16@?20@?28B36"
- "width"

```
