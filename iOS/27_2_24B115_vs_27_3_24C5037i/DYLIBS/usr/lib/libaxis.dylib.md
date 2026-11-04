## libaxis.dylib

> `/usr/lib/libaxis.dylib`

```diff

-8.1.15.0.0
-  __TEXT.__text: 0x54f480
-  __TEXT.__const: 0xf8a4
-  __TEXT.__gcc_except_tab: 0x48268
-  __TEXT.__cstring: 0x17928
-  __TEXT.__unwind_info: 0x12598
+8.2.1.0.0
+  __TEXT.__text: 0x539b00
+  __TEXT.__const: 0xf804
+  __TEXT.__gcc_except_tab: 0x46f38
+  __TEXT.__cstring: 0x17881
+  __TEXT.__unwind_info: 0x11ee8
   __TEXT.__eh_frame: 0x88
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xc0
   __DATA_CONST.__weak_got: 0x680
   __DATA_CONST.__got: 0x1b8
-  __AUTH_CONST.__const: 0x9138
-  __AUTH_CONST.__weak_auth_got: 0x450
+  __AUTH_CONST.__const: 0x9148
+  __AUTH_CONST.__weak_auth_got: 0x3d0
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__data: 0x10
   __AUTH.__thread_vars: 0x288

   __DATA.__common: 0x8
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 9983
-  Symbols:   2776
-  CStrings:  2079
+  Functions: 9718
+  Symbols:   2708
+  CStrings:  2078
 
Symbols:
+ __ZNK4axis9LineSeg2D24intersection_with_circleERKNS_11PointData2DEd
+ __ZNK4axis9LineSeg2D25intersection_with_obroundERKNS_11PointData2DES3_d
+ __ZNK5terra19TriangulatedTerrain18get_elevation_implERKN4axis11PointData2DERiS5_
- __ZN4axis11InterpolateILi2EE8linearLLERKNS_10Polyline2DEd
- __ZN4axis11InterpolateILi3EE8linearLLERKN5terra10Polyline3DEd
- __ZN4axis14NormalFormBaseILi2EE11getWithInfoENSt3__110shared_ptrINS_12MultiPoint2DEEERNS2_6vectorIiNS2_9allocatorIiEEEERKNS1_7OptionsE
- __ZN4axis14NormalFormBaseILi3EE11getWithInfoENSt3__110shared_ptrIN5terra12MultiPoint3DEEERNS2_6vectorIiNS2_9allocatorIiEEEERKNS1_7OptionsE
- __ZN4axis14SpatialBooleanILi2EE20setEnableFastBooleanEb
- __ZN4axis14SpatialBooleanILi3EE20setEnableFastBooleanEb
- __ZN4axis7DensifyILi2EE12ifLongerThanERKNS_10Geometry2DEd
- __ZN4axis7DensifyILi2EE12ifLongerThanERKNS_10Polyline2DEd
- __ZN4axis7DensifyILi2EE12ifLongerThanERKNS_9Polygon2DEd
- __ZN4axis7DensifyILi2EE16ifLongerThanSnapERKNS_10Geometry2DEdd
- __ZN4axis7DensifyILi2EE16ifLongerThanSnapERKNS_10Polyline2DEdd
- __ZN4axis7DensifyILi2EE16ifLongerThanSnapERKNS_9Polygon2DEdd
- __ZN4axis7DensifyILi3EE12ifLongerThanERKN5terra10Geometry3DEd
- __ZN4axis7DensifyILi3EE12ifLongerThanERKN5terra10Polyline3DEd
- __ZN4axis7DensifyILi3EE12ifLongerThanERKN5terra9Polygon3DEd
- __ZN4axis7DensifyILi3EE16ifLongerThanSnapERKN5terra10Geometry3DEdd
- __ZN4axis7DensifyILi3EE16ifLongerThanSnapERKN5terra10Polyline3DEdd
- __ZN4axis7DensifyILi3EE16ifLongerThanSnapERKN5terra9Polygon3DEdd
- __ZN5terra21TerrainSimplificationINS_5TMeshEE11setBoundaryENSt3__110shared_ptrINS_14MultiPolygon3DEEE
- __ZN5terra21TerrainSimplificationINS_5TMeshEE12extractTMeshERNSt3__16vectorIdNS3_9allocatorIdEEEERNS4_IiNS5_IiEEEE
- __ZN5terra21TerrainSimplificationINS_5TMeshEE12extractTMeshEv
- __ZN5terra21TerrainSimplificationINS_5TMeshEE13setZToleranceEd
- __ZN5terra21TerrainSimplificationINS_5TMeshEE14getMaxVerticesEv
- __ZN5terra21TerrainSimplificationINS_5TMeshEE14setInteractiveEb
- __ZN5terra21TerrainSimplificationINS_5TMeshEE14setMaxVerticesEm
- __ZN5terra21TerrainSimplificationINS_5TMeshEE15getInputIndicesEv
- __ZN5terra21TerrainSimplificationINS_5TMeshEE15simplifyTerrainEv
- __ZN5terra21TerrainSimplificationINS_5TMeshEE17setMaxAspectRatioEd
- __ZN5terra21TerrainSimplificationINS_5TMeshEE26setMinRelativeTriangleSizeEd
- __ZN5terra21TerrainSimplificationINS_5TMeshEE38configureBoundaryCollinearPointRemovalEd
- __ZN5terra21TerrainSimplificationINS_9GeoRasterIfEEE11setBoundaryENSt3__110shared_ptrINS_14MultiPolygon3DEEE
- __ZN5terra21TerrainSimplificationINS_9GeoRasterIfEEE12extractTMeshERNSt3__16vectorIdNS4_9allocatorIdEEEERNS5_IiNS6_IiEEEE
- __ZN5terra21TerrainSimplificationINS_9GeoRasterIfEEE12extractTMeshEv
- __ZN5terra21TerrainSimplificationINS_9GeoRasterIfEEE13setZToleranceEd
- __ZN5terra21TerrainSimplificationINS_9GeoRasterIfEEE14getMaxVerticesEv
- __ZN5terra21TerrainSimplificationINS_9GeoRasterIfEEE14setInteractiveEb
- __ZN5terra21TerrainSimplificationINS_9GeoRasterIfEEE14setMaxVerticesEm
- __ZN5terra21TerrainSimplificationINS_9GeoRasterIfEEE15getInputIndicesEv
- __ZN5terra21TerrainSimplificationINS_9GeoRasterIfEEE15simplifyTerrainEv
- __ZN5terra21TerrainSimplificationINS_9GeoRasterIfEEE17setMaxAspectRatioEd
- __ZN5terra21TerrainSimplificationINS_9GeoRasterIfEEE26setMinRelativeTriangleSizeEd
- __ZN5terra21TerrainSimplificationINS_9GeoRasterIfEEE38configureBoundaryCollinearPointRemovalEd
- __ZN5terra9GeoRasterIfE10columnFromEiRKS1_i
- __ZN5terra9GeoRasterIfE10columnIntoEiiRKS1_i
- __ZN5terra9GeoRasterIfE7rowFromEiRKS1_i
- __ZN5terra9GeoRasterIfE7rowIntoEiiRKS1_i
- __ZN5terra9GeoRasterIfE8getValueEii
- __ZN5terra9GeoRasterIfE8setValueEiif
- __ZNK4axis14SpatialBooleanILi2EE20getEnableFastBooleanEv
- __ZNK4axis14SpatialBooleanILi3EE20getEnableFastBooleanEv
- __ZNK5terra21TerrainSimplificationINS_5TMeshEE17getMaxAspectRatioEv
- __ZNK5terra21TerrainSimplificationINS_5TMeshEE26getMinRelativeTriangleSizeEv
- __ZNK5terra21TerrainSimplificationINS_9GeoRasterIfEEE17getMaxAspectRatioEv
- __ZNK5terra21TerrainSimplificationINS_9GeoRasterIfEEE26getMinRelativeTriangleSizeEv
- __ZNK5terra9GeoRasterIfE10getNumRowsEv
- __ZNK5terra9GeoRasterIfE11numVerticesEv
- __ZNK5terra9GeoRasterIfE12getPixelBBoxEii
- __ZNK5terra9GeoRasterIfE13getEmptyValueEv
- __ZNK5terra9GeoRasterIfE13getNumColumnsEv
- __ZNK5terra9GeoRasterIfE14asMultiPoint3DEv
- __ZNK5terra9GeoRasterIfE14getRasterPixelEv
- __ZNK5terra9GeoRasterIfE19isValuesInitializedEv
- __ZNK5terra9GeoRasterIfE7getBBoxEv
- __ZNK5terra9GeoRasterIfE8getPointERKN4axis11PointData2DE
- __ZNK5terra9GeoRasterIfE8getValueEii
- __ZNK5terra9GeoRasterIfE8sameGridERKS1_
- __ZNK5terra9GeoRasterIfE9getPixelXEi
- __ZNK5terra9GeoRasterIfE9getPixelYEi
- __ZNK5terra9GeoRasterIfE9getVertexEi
- __ZNK5terra9GeoRasterIfE9getVertexEii
- __ZNK5terra9GeoRasterIfE9subRasterEiiii
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Cartesian/function_objects.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Compact_container.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Constrained_Delaunay_triangulation_2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Constrained_triangulation_2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Constrained_triangulation_face_base_2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Constrained_triangulation_plus_2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Convex_hull_2/ch_akl_toussaint_impl.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Convex_hull_2/ch_graham_andrew_impl.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/HalfedgeDS_list.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Handle.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/In_place_list.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Intersections_2/Iso_rectangle_2_Line_2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Intersections_2/Iso_rectangle_2_Ray_2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Intersections_2/Iso_rectangle_2_Segment_2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Intersections_2/Line_2_Line_2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Intersections_2/Segment_2_Segment_2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Intersections_3/internal/Segment_3_Triangle_3_do_intersect.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Intersections_3/internal/Triangle_3_Triangle_3_do_intersect.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Interval_nt.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Kernel/function_objects.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Lazy.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Lazy_exact_nt.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Min_quadrilateral_traits_2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Parabola_2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Parabola_segment_2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Partition_2/Partition_vertex_map.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Partition_2/Rotation_tree_2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Partition_2/Rotation_tree_2_impl.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Partition_2/Vertex_visibility_graph_2_impl.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Partition_2/partition_optimal_convex_2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Polygon_2/Polygon_2_algorithms_impl.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Polygon_2/Polygon_2_simplicity.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Polygon_mesh_processing/orient_polygon_soup.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Polygon_mesh_processing/polygon_soup_to_polygon_mesh.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Polygon_mesh_processing/self_intersections.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Polyhedron_incremental_builder_3.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Polyline_simplification_2/simplify.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_2/Are_parallel_C2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_2/Are_same_points_C2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_2/Are_same_segments_C2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_2/Arrangement_type_C2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_2/Basic_predicates_C2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_2/Compare_x_2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_2/Compare_y_2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_2/Construct_storage_site_2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_2/Constructions_C2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_2/Finite_edge_interior_conflict_C2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_2/Infinite_edge_interior_conflict_C2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_2/Oriented_side_C2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_2/Oriented_side_of_bisector_C2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_2/Segment_Delaunay_graph_2_impl.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_2/Vertex_conflict_C2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_2/Voronoi_vertex_sqrt_field_new_C2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_simple_site_2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_simple_storage_site_2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_site_2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_storage_site_2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_storage_site_with_info_2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/TDS_2/internal/edge_list.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Time_stamper.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Triangulation_2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Triangulation_2/internal/Triangulation_line_face_circulator_2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Triangulation_data_structure_2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Triangulation_ds_circulators_2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Triangulation_ds_face_base_2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Triangulation_ds_iterators_2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Triangulation_utils_2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/Uncertain.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/boost/graph/Euler_operations.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/boost/graph/helpers.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/circulator.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/iterator.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/leda_rational.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/min_quadrilateral_2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/partition_is_valid_2.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/CGAL/predicates/kernel_ftC3.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/boost/multiprecision/complex_adaptor.hpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/boost/multiprecision/cpp_bin_float.hpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/boost/multiprecision/cpp_bin_float/io.hpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/boost/multiprecision/cpp_int.hpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/boost/multiprecision/cpp_int/divide.hpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/boost/multiprecision/cpp_int/misc.hpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/boost/multiprecision/detail/functions/trig.hpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/boost/multiprecision/detail/number_base.hpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/local/include/boost/multiprecision/integer.hpp"
+ "TriangulatedTerrain::compute_segment_edge_intersection(shallow)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Cartesian/function_objects.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Compact_container.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Constrained_Delaunay_triangulation_2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Constrained_triangulation_2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Constrained_triangulation_face_base_2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Constrained_triangulation_plus_2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Convex_hull_2/ch_akl_toussaint_impl.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Convex_hull_2/ch_graham_andrew_impl.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/HalfedgeDS_list.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Handle.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/In_place_list.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Intersections_2/Iso_rectangle_2_Line_2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Intersections_2/Iso_rectangle_2_Ray_2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Intersections_2/Iso_rectangle_2_Segment_2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Intersections_2/Line_2_Line_2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Intersections_2/Segment_2_Segment_2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Intersections_3/internal/Segment_3_Triangle_3_do_intersect.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Intersections_3/internal/Triangle_3_Triangle_3_do_intersect.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Interval_nt.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Kernel/function_objects.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Lazy.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Lazy_exact_nt.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Min_quadrilateral_traits_2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Parabola_2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Parabola_segment_2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Partition_2/Partition_vertex_map.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Partition_2/Rotation_tree_2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Partition_2/Rotation_tree_2_impl.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Partition_2/Vertex_visibility_graph_2_impl.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Partition_2/partition_optimal_convex_2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Polygon_2/Polygon_2_algorithms_impl.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Polygon_2/Polygon_2_simplicity.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Polygon_mesh_processing/orient_polygon_soup.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Polygon_mesh_processing/polygon_soup_to_polygon_mesh.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Polygon_mesh_processing/self_intersections.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Polyhedron_incremental_builder_3.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Polyline_simplification_2/simplify.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_2/Are_parallel_C2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_2/Are_same_points_C2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_2/Are_same_segments_C2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_2/Arrangement_type_C2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_2/Basic_predicates_C2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_2/Compare_x_2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_2/Compare_y_2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_2/Construct_storage_site_2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_2/Constructions_C2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_2/Finite_edge_interior_conflict_C2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_2/Infinite_edge_interior_conflict_C2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_2/Oriented_side_C2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_2/Oriented_side_of_bisector_C2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_2/Segment_Delaunay_graph_2_impl.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_2/Vertex_conflict_C2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_2/Voronoi_vertex_sqrt_field_new_C2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_simple_site_2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_simple_storage_site_2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_site_2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_storage_site_2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Segment_Delaunay_graph_storage_site_with_info_2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/TDS_2/internal/edge_list.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Time_stamper.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Triangulation_2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Triangulation_2/internal/Triangulation_line_face_circulator_2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Triangulation_data_structure_2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Triangulation_ds_circulators_2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Triangulation_ds_face_base_2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Triangulation_ds_iterators_2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Triangulation_utils_2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/Uncertain.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/boost/graph/Euler_operations.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/boost/graph/helpers.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/circulator.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/iterator.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/leda_rational.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/min_quadrilateral_2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/partition_is_valid_2.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/CGAL/predicates/kernel_ftC3.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/boost/multiprecision/complex_adaptor.hpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/boost/multiprecision/cpp_bin_float.hpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/boost/multiprecision/cpp_bin_float/io.hpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/boost/multiprecision/cpp_int.hpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/boost/multiprecision/cpp_int/divide.hpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/boost/multiprecision/cpp_int/misc.hpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/boost/multiprecision/detail/functions/trig.hpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/boost/multiprecision/detail/number_base.hpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/boost/multiprecision/integer.hpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AxisGeometry/src/axis/predicates/GetDE9IM.hpp"
- "The GetDE9IM spatial predicate on geometries with mixed dimension is not supported."
```
