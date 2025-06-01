## PhysicsKit

> `/System/Library/PrivateFrameworks/PhysicsKit.framework/PhysicsKit`

```diff

-40.0.3.0.0
-  __TEXT.__text: 0x3d9b0
+40.4.2.0.0
+  __TEXT.__text: 0x4051c
   __TEXT.__auth_stubs: 0x710
   __TEXT.__objc_methlist: 0x1574
-  __TEXT.__gcc_except_tab: 0x23e0
+  __TEXT.__gcc_except_tab: 0x2408
   __TEXT.__const: 0x1c04
-  __TEXT.__cstring: 0x636
-  __TEXT.__unwind_info: 0x1a44
-  __TEXT.__eh_frame: 0x150
+  __TEXT.__cstring: 0x1928
+  __TEXT.__unwind_info: 0x1a9c
+  __TEXT.__eh_frame: 0x164
   __TEXT.__objc_classname: 0x243
   __TEXT.__objc_methname: 0x1fb6
   __TEXT.__objc_methtype: 0x2093

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x1520
   __DATA_CONST.__objc_selrefs: 0xb28
+  __DATA_CONST.__objc_classrefs: 0x120
+  __DATA_CONST.__objc_superrefs: 0xb0
   __AUTH_CONST.__objc_const: 0x0
   __AUTH_CONST.__cfstring: 0xd60
   __AUTH_CONST.__auth_got: 0x398
   __DATA.__got_weak: 0x8
-  __DATA.__objc_classrefs: 0x120
-  __DATA.__objc_superrefs: 0xb0
   __DATA.__objc_ivar: 0x148
   __DATA.__data: 0x12c
   __DATA.__bss: 0x30

   __DATA_DIRTY.__objc_const: 0xdb8
   __DATA_DIRTY.__objc_data: 0x7d0
   __DATA_DIRTY.__data: 0x20
-  __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1282A0EF-53BF-3343-9D7F-E1DD0AE98EBE
-  Functions: 1482
-  Symbols:   3923
-  CStrings:  850
+  UUID: 0C60DD03-DCEB-32D5-A571-A460658D46D0
+  Functions: 1659
+  Symbols:   4273
+  CStrings:  1066
 
Symbols:
+ -[PKPhysicsBody setDensity:].cold.1
+ GCC_except_table114
+ GCC_except_table121
+ GCC_except_table124
+ GCC_except_table132
+ GCC_except_table136
+ GCC_except_table140
+ GCC_except_table151
+ GCC_except_table161
+ GCC_except_table168
+ __Z10b2DistanceP16b2DistanceOutputP14b2SimplexCachePK15b2DistanceInput.cold.1
+ __Z10b2DistanceP16b2DistanceOutputP14b2SimplexCachePK15b2DistanceInput.cold.2
+ __Z10b2DistanceP16b2DistanceOutputP14b2SimplexCachePK15b2DistanceInput.cold.3
+ __Z14b2TimeOfImpactP11b2TOIOutputPK10b2TOIInput.cold.1
+ __Z17b2CollidePolygonsP10b2ManifoldPK14b2PolygonShapeRK11b2TransformS3_S6_.cold.1
+ __Z22b2CollideEdgeAndCircleP10b2ManifoldPK11b2EdgeShapeRK11b2TransformPK13b2CircleShapeS6_.cold.1
+ __ZL16b2EdgeSeparationPK14b2PolygonShapeRK11b2TransformiS1_S4_.cold.1
+ __ZN11b2GearJoint8SetRatioEf.cold.1
+ __ZN11b2GearJointC2EPK14b2GearJointDef.cold.1
+ __ZN11b2GearJointC2EPK14b2GearJointDef.cold.2
+ __ZN12b2ChainShape11CreateChainEPK6b2Vec2i.cold.1
+ __ZN12b2MouseJoint23InitVelocityConstraintsERK12b2SolverData.cold.1
+ __ZN12b2MouseJointC2EPK15b2MouseJointDef.cold.1
+ __ZN12b2MouseJointC2EPK15b2MouseJointDef.cold.2
+ __ZN12b2MouseJointC2EPK15b2MouseJointDef.cold.3
+ __ZN12b2MouseJointC2EPK15b2MouseJointDef.cold.4
+ __ZN13b2DynamicTree10InsertLeafEi.cold.1
+ __ZN13b2DynamicTree10InsertLeafEi.cold.2
+ __ZN13b2DynamicTree12AllocateNodeEv.cold.1
+ __ZN13b2DynamicTree12DestroyProxyEi.cold.1
+ __ZN13b2DynamicTree12DestroyProxyEi.cold.2
+ __ZN13b2DynamicTree7BalanceEi.cold.1
+ __ZN13b2DynamicTree7BalanceEi.cold.2
+ __ZN13b2DynamicTree7BalanceEi.cold.3
+ __ZN13b2DynamicTree7BalanceEi.cold.4
+ __ZN13b2DynamicTree7BalanceEi.cold.5
+ __ZN13b2DynamicTree7BalanceEi.cold.6
+ __ZN13b2DynamicTree7BalanceEi.cold.7
+ __ZN13b2DynamicTree7BalanceEi.cold.8
+ __ZN13b2DynamicTree7BalanceEi.cold.9
+ __ZN13b2DynamicTree8FreeNodeEi.cold.1
+ __ZN13b2DynamicTree8FreeNodeEi.cold.2
+ __ZN13b2DynamicTree9MoveProxyEiRK6b2AABBRK6b2Vec2.cold.1
+ __ZN13b2DynamicTree9MoveProxyEiRK6b2AABBRK6b2Vec2.cold.2
+ __ZN13b2PulleyJointC2EPK16b2PulleyJointDef.cold.1
+ __ZN15b2CircleContactC2EP9b2FixtureS1_.cold.1
+ __ZN15b2CircleContactC2EP9b2FixtureS1_.cold.2
+ __ZN15b2ContactSolver24SolveVelocityConstraintsEv.cold.1
+ __ZN15b2ContactSolver29InitializeVelocityConstraintsEv.cold.1
+ __ZN15b2ContactSolverC2EP18b2ContactSolverDefRKNSt3__16vectorIP6b2BodyNS2_9allocatorIS5_EEEERKNS3_IP9b2ContactNS6_ISC_EEEE.cold.1
+ __ZN15b2DistanceProxy3SetEPK7b2Shapei.cold.1
+ __ZN15b2DistanceProxy3SetEPK7b2Shapei.cold.2
+ __ZN15b2DistanceProxy3SetEPK7b2Shapei.cold.3
+ __ZN15b2FrictionJoint11SetMaxForceEf.cold.1
+ __ZN15b2FrictionJoint12SetMaxTorqueEf.cold.1
+ __ZN15b2RevoluteJoint9SetLimitsEff.cold.1
+ __ZN16b2ContactManager13QueryCallbackEi.cold.1
+ __ZN16b2ContactManager13QueryCallbackEi.cold.2
+ __ZN16b2ContactManager14FindMinimumTOIERP9b2ContactRf.cold.1
+ __ZN16b2ContactManager15FindNewContactsEv.cold.1
+ __ZN16b2ContactManager15FindNewContactsEv.cold.2
+ __ZN16b2ContactManager15FindNewContactsEv.cold.3
+ __ZN16b2PolygonContactC2EP9b2FixtureS1_.cold.1
+ __ZN16b2PolygonContactC2EP9b2FixtureS1_.cold.2
+ __ZN16b2PrismaticJoint9SetLimitsEff.cold.1
+ __ZN16b2PulleyJointDef10InitializeEP6b2BodyS1_RK6b2Vec2S4_S4_S4_f.cold.1
+ __ZN16b2StackAllocator4FreeEPv.cold.1
+ __ZN16b2StackAllocator4FreeEPv.cold.2
+ __ZN16b2StackAllocator8AllocateEi.cold.1
+ __ZN20b2SeparationFunction10InitializeEPK14b2SimplexCachePK15b2DistanceProxyRK7b2SweepS5_S8_f.cold.1
+ __ZN20b2SeparationFunction10InitializeEPK14b2SimplexCachePK15b2DistanceProxyRK7b2SweepS5_S8_f.cold.2
+ __ZN20b2SeparationFunction10InitializeEPK14b2SimplexCachePK15b2DistanceProxyRK7b2SweepS5_S8_f.cold.3
+ __ZN20b2SeparationFunction10InitializeEPK14b2SimplexCachePK15b2DistanceProxyRK7b2SweepS5_S8_f.cold.4
+ __ZN20b2SeparationFunction10InitializeEPK14b2SimplexCachePK15b2DistanceProxyRK7b2SweepS5_S8_f.cold.5
+ __ZN20b2SeparationFunction10InitializeEPK14b2SimplexCachePK15b2DistanceProxyRK7b2SweepS5_S8_f.cold.6
+ __ZN20b2SeparationFunction10InitializeEPK14b2SimplexCachePK15b2DistanceProxyRK7b2SweepS5_S8_f.cold.7
+ __ZN20b2SeparationFunction10InitializeEPK14b2SimplexCachePK15b2DistanceProxyRK7b2SweepS5_S8_f.cold.8
+ __ZN20b2SeparationFunction10InitializeEPK14b2SimplexCachePK15b2DistanceProxyRK7b2SweepS5_S8_f.cold.9
+ __ZN22b2EdgeAndCircleContactC2EP9b2FixtureS1_.cold.1
+ __ZN22b2EdgeAndCircleContactC2EP9b2FixtureS1_.cold.2
+ __ZN23b2ChainAndCircleContactC2EP9b2FixtureiS1_i.cold.1
+ __ZN23b2ChainAndCircleContactC2EP9b2FixtureiS1_i.cold.2
+ __ZN23b2EdgeAndPolygonContactC2EP9b2FixtureS1_.cold.1
+ __ZN23b2EdgeAndPolygonContactC2EP9b2FixtureS1_.cold.2
+ __ZN24b2ChainAndPolygonContactC2EP9b2FixtureiS1_i.cold.1
+ __ZN24b2ChainAndPolygonContactC2EP9b2FixtureiS1_i.cold.2
+ __ZN24b2PositionSolverManifold10InitializeEP27b2ContactPositionConstraintRK11b2TransformS4_i.cold.1
+ __ZN24b2QuadtreeAndEdgeContactC2EP9b2FixtureiS1_i.cold.1
+ __ZN24b2QuadtreeAndEdgeContactC2EP9b2FixtureiS1_i.cold.2
+ __ZN25b2PolygonAndCircleContactC2EP9b2FixtureS1_.cold.1
+ __ZN25b2PolygonAndCircleContactC2EP9b2FixtureS1_.cold.2
+ __ZN25b2QuadtreeAndChainContactC2EP9b2FixtureiS1_i.cold.1
+ __ZN25b2QuadtreeAndChainContactC2EP9b2FixtureiS1_i.cold.2
+ __ZN26MechanicsCollisionCallback13ReportFixtureEP9b2Fixture.cold.1
+ __ZN26b2QuadtreeAndCircleContactC2EP9b2FixtureiS1_i.cold.1
+ __ZN26b2QuadtreeAndCircleContactC2EP9b2FixtureiS1_i.cold.2
+ __ZN27b2QuadtreeAndPolygonContactC2EP9b2FixtureiS1_i.cold.1
+ __ZN27b2QuadtreeAndPolygonContactC2EP9b2FixtureiS1_i.cold.2
+ __ZN28b2QuadtreeAndQuadtreeContactC2EP9b2FixtureiS1_i.cold.1
+ __ZN28b2QuadtreeAndQuadtreeContactC2EP9b2FixtureiS1_i.cold.2
+ __ZN6b2Body11SetMassDataEPK10b2MassData.cold.1
+ __ZN6b2Body11SetMassDataEPK10b2MassData.cold.2
+ __ZN6b2Body12SetTransformERK6b2Vec2f.cold.1
+ __ZN6b2Body13CreateFixtureEPK12b2FixtureDef.cold.1
+ __ZN6b2Body14DestroyFixtureEP9b2Fixture.cold.1
+ __ZN6b2Body14DestroyFixtureEP9b2Fixture.cold.2
+ __ZN6b2Body14DestroyFixtureEP9b2Fixture.cold.3
+ __ZN6b2Body14DestroyFixtureEP9b2Fixture.cold.4
+ __ZN6b2Body7SetTypeE10b2BodyType.cold.1
+ __ZN6b2Body9SetActiveEb.cold.1
+ __ZN6b2BodyC2EPK9b2BodyDefP7b2World.cold.1
+ __ZN6b2BodyC2EPK9b2BodyDefP7b2World.cold.2
+ __ZN6b2BodyC2EPK9b2BodyDefP7b2World.cold.3
+ __ZN6b2BodyC2EPK9b2BodyDefP7b2World.cold.4
+ __ZN6b2BodyC2EPK9b2BodyDefP7b2World.cold.5
+ __ZN6b2BodyC2EPK9b2BodyDefP7b2World.cold.6
+ __ZN6b2Rope10InitializeEPK9b2RopeDef.cold.1
+ __ZN7b2Joint6CreateEPK10b2JointDef.cold.1
+ __ZN7b2JointC2EPK10b2JointDef.cold.1
+ __ZN7b2World10CreateBodyEPK9b2BodyDef.cold.1
+ __ZN7b2World11CreateJointEPK10b2JointDef.cold.1
+ __ZN7b2World11DestroyBodyEP6b2Body.cold.1
+ __ZN7b2World11DestroyBodyEP6b2Body.cold.2
+ __ZN7b2World12DestroyJointEP7b2Joint.cold.1
+ __ZN7b2World12DestroyJointEP7b2Joint.cold.2
+ __ZN7b2World13DrawDebugDataEv.cold.1
+ __ZN8b2Island8SolveTOIERK10b2TimeStepiif.cold.1
+ __ZN8b2Island8SolveTOIERK10b2TimeStepiif.cold.2
+ __ZN9b2Contact6CreateEP9b2FixtureiS1_i.cold.1
+ __ZN9b2Contact6CreateEP9b2FixtureiS1_i.cold.2
+ __ZN9b2Contact7AddTypeEPFPS_P9b2FixtureiS2_iEN7b2Shape4TypeES6_.cold.1
+ __ZN9b2Contact7AddTypeEPFPS_P9b2FixtureiS2_iEN7b2Shape4TypeES6_.cold.2
+ __ZN9b2Contact7DestroyEPS_.cold.1
+ __ZN9b2Simplex9ReadCacheEPK14b2SimplexCachePK15b2DistanceProxyRK11b2TransformS5_S8_.cold.1
+ __ZN9b2Simplex9ReadCacheEPK14b2SimplexCachePK15b2DistanceProxyRK11b2TransformS5_S8_.cold.2
+ __ZN9b2Simplex9ReadCacheEPK14b2SimplexCachePK15b2DistanceProxyRK11b2TransformS5_S8_.cold.3
+ __ZN9b2Simplex9ReadCacheEPK14b2SimplexCachePK15b2DistanceProxyRK11b2TransformS5_S8_.cold.4
+ __ZN9b2Simplex9ReadCacheEPK14b2SimplexCachePK15b2DistanceProxyRK11b2TransformS5_S8_.cold.5
+ __ZNK12b2ChainShape11ComputeAABBEP6b2AABBRK11b2Transformi.cold.1
+ __ZNK12b2ChainShape12GetChildEdgeEP11b2EdgeShapei.cold.1
+ __ZNK12b2ChainShape7RayCastEP15b2RayCastOutputRK14b2RayCastInputRK11b2Transformi.cold.1
+ __ZNK12b2ChainShape9GetVertexEi
+ __ZNK12b2ChainShape9GetVertexEi.cold.1
+ __ZNK13b2DynamicTree13ComputeHeightEi.cold.1
+ __ZNK13b2DynamicTree13GetMaxBalanceEv.cold.1
+ __ZNK13b2DynamicTree15ValidateMetricsEi.cold.1
+ __ZNK13b2DynamicTree15ValidateMetricsEi.cold.2
+ __ZNK13b2DynamicTree15ValidateMetricsEi.cold.3
+ __ZNK13b2DynamicTree15ValidateMetricsEi.cold.4
+ __ZNK13b2DynamicTree15ValidateMetricsEi.cold.5
+ __ZNK13b2DynamicTree15ValidateMetricsEi.cold.6
+ __ZNK13b2DynamicTree15ValidateMetricsEi.cold.7
+ __ZNK13b2DynamicTree17ValidateStructureEi.cold.1
+ __ZNK13b2DynamicTree17ValidateStructureEi.cold.2
+ __ZNK13b2DynamicTree17ValidateStructureEi.cold.3
+ __ZNK13b2DynamicTree17ValidateStructureEi.cold.4
+ __ZNK13b2DynamicTree17ValidateStructureEi.cold.5
+ __ZNK13b2DynamicTree17ValidateStructureEi.cold.6
+ __ZNK13b2DynamicTree17ValidateStructureEi.cold.7
+ __ZNK13b2DynamicTree7RayCastI21b2WorldRayCastWrapperEEvPT_RK14b2RayCastInput.cold.1
+ __ZNK13b2DynamicTree8ValidateEv.cold.1
+ __ZNK13b2DynamicTree8ValidateEv.cold.2
+ __ZNK13b2DynamicTree8ValidateEv.cold.3
+ __ZNK14b2PolygonShape11ComputeMassEP10b2MassDataf.cold.1
+ __ZNK14b2PolygonShape7RayCastEP15b2RayCastOutputRK14b2RayCastInputRK11b2Transformi.cold.1
+ __ZNK16b2ContactManager15GetFixtureProxyEi
+ __ZNK16b2ContactManager15GetFixtureProxyEi.cold.1
+ __ZNK20b2SeparationFunction17FindMinSeparationEPiS0_f.cold.1
+ __ZNK20b2SeparationFunction17FindMinSeparationEPiS0_f.cold.2
+ __ZNK20b2SeparationFunction17FindMinSeparationEPiS0_f.cold.3
+ __ZNK20b2SeparationFunction17FindMinSeparationEPiS0_f.cold.4
+ __ZNK20b2SeparationFunction17FindMinSeparationEPiS0_f.cold.5
+ __ZNK20b2SeparationFunction8EvaluateEiif.cold.1
+ __ZNK20b2SeparationFunction8EvaluateEiif.cold.2
+ __ZNK20b2SeparationFunction8EvaluateEiif.cold.3
+ __ZNK20b2SeparationFunction8EvaluateEiif.cold.4
+ __ZNK20b2SeparationFunction8EvaluateEiif.cold.5
+ __ZNK9b2Simplex15GetClosestPointEv.cold.1
+ __ZNK9b2Simplex15GetClosestPointEv.cold.2
+ __ZNK9b2Simplex16GetWitnessPointsEP6b2Vec2S1_.cold.1
+ __ZNK9b2Simplex16GetWitnessPointsEP6b2Vec2S1_.cold.2
+ __ZNK9b2Simplex18GetSearchDirectionEv.cold.1
+ __ZNK9b2Simplex9GetMetricEv.cold.1
+ __ZNK9b2Simplex9GetMetricEv.cold.2
+ __ZNKSt3__111__move_loopINS_17_ClassicAlgPolicyEEclB8ue170006IPNS_8weak_ptrI8PKCFieldEES7_S7_EENS_4pairIT_T1_EES9_T0_SA_
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorINS_10shared_ptrI8PKCFieldEEEENS_16reverse_iteratorIPS4_EEEclB8ue170006Ev
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorINS_8weak_ptrI8PKCFieldEEEENS_16reverse_iteratorIPS4_EEEclB8ue170006Ev
+ __ZNKSt3__16vectorI14b2FixtureProxyNS_9allocatorIS1_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorI6b2Vec2NS_9allocatorIS1_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorI7CGPointNS_9allocatorIS1_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorI7PKPointNS_9allocatorIS1_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIDv2_fNS_9allocatorIS1_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIDv4_fNS_9allocatorIS1_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIN17PKDebugDrawPacket6color4ENS_9allocatorIS2_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorINS_10shared_ptrI8PKCFieldEENS_9allocatorIS3_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorINS_8weak_ptrI8PKCFieldEENS_9allocatorIS3_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIP12QuadTreeNodeNS_9allocatorIS2_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIP14PKPhysicsShapeNS_9allocatorIS2_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIP6b2BodyNS_9allocatorIS2_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIP7b2JointNS_9allocatorIS2_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIP8PKCFieldNS_9allocatorIS2_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIP8QuadTreeNS_9allocatorIS2_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIP9b2ContactNS_9allocatorIS2_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIaNS_9allocatorIaEEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt9type_infoeqB8ue170006ERKS_
+ __ZNSt12length_errorC1B8ue170006EPKc
+ __ZNSt3__110__function12__value_funcIFvffiEEC2B8ue170006ERKS3_
+ __ZNSt3__110__function12__value_funcIFvffiEED2B8ue170006Ev
+ __ZNSt3__110shared_ptrI6PKPathEC2B8ue170006IS1_vEEPT_
+ __ZNSt3__114__split_bufferINS_10shared_ptrI8PKCFieldEERNS_9allocatorIS3_EEE5clearB8ue170006Ev
+ __ZNSt3__114__split_bufferINS_8weak_ptrI8PKCFieldEERNS_9allocatorIS3_EEE5clearB8ue170006Ev
+ __ZNSt3__115allocate_sharedB8ue170006I12PKCFieldDragNS_9allocatorIS1_EEJEvEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ue170006I12PKCFieldUserNS_9allocatorIS1_EEJPvEvEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ue170006I13PKCFieldNoiseNS_9allocatorIS1_EEJEvEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ue170006I14PKCFieldSpringNS_9allocatorIS1_EEJEvEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ue170006I14PKCFieldVortexNS_9allocatorIS1_EEJEvEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ue170006I16PKCFieldElectricNS_9allocatorIS1_EEJEvEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ue170006I16PKCFieldMagneticNS_9allocatorIS1_EEJEvEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ue170006I16PKCFieldVelocityNS_9allocatorIS1_EEJEvEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ue170006I18PKCFieldTurbulenceNS_9allocatorIS1_EEJEvEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ue170006I21PKCFieldLinearGravityNS_9allocatorIS1_EEJEvEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ue170006I21PKCFieldRadialGravityNS_9allocatorIS1_EEJEvEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ue170006I6PKPathNS_9allocatorIS1_EEJRS1_EvEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ue170006I7PKCGridNS_9allocatorIS1_EEJEvEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ue170006I8QuadTreeNS_9allocatorIS1_EEJfffffEvEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorI14b2FixtureProxyEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorI6b2Vec2EEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorI7CGPointEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorI7PKPointEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorIDv2_fEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorIDv4_fEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorIN17PKDebugDrawPacket6color4EEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorINS_10shared_ptrI8PKCFieldEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorINS_8weak_ptrI8PKCFieldEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorIP12QuadTreeNodeEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorIP14PKPhysicsShapeEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorIP6b2BodyEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorIP7b2JointEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorIP8PKCFieldEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorIP8QuadTreeEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorIP9b2ContactEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorIiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__shared_weak_count16__release_sharedB8ue170006Ev
+ __ZNSt3__120__shared_ptr_emplaceI12PKCFieldDragNS_9allocatorIS1_EEEC2B8ue170006IJEEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI12PKCFieldUserNS_9allocatorIS1_EEEC2B8ue170006IJPvEEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI13PKCFieldNoiseNS_9allocatorIS1_EEEC2B8ue170006IJEEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI14PKCFieldSpringNS_9allocatorIS1_EEEC2B8ue170006IJEEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI14PKCFieldVortexNS_9allocatorIS1_EEEC2B8ue170006IJEEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI16PKCFieldElectricNS_9allocatorIS1_EEEC2B8ue170006IJEEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI16PKCFieldMagneticNS_9allocatorIS1_EEEC2B8ue170006IJEEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI16PKCFieldVelocityNS_9allocatorIS1_EEEC2B8ue170006IJEEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI18PKCFieldTurbulenceNS_9allocatorIS1_EEEC2B8ue170006IJEEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI21PKCFieldLinearGravityNS_9allocatorIS1_EEEC2B8ue170006IJEEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI21PKCFieldRadialGravityNS_9allocatorIS1_EEEC2B8ue170006IJEEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI6PKPathNS_9allocatorIS1_EEEC2B8ue170006IJRS1_EEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI7PKCGridNS_9allocatorIS1_EEEC2B8ue170006IJEEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI8QuadTreeNS_9allocatorIS1_EEEC2B8ue170006IJfffffEEES3_DpOT_
+ __ZNSt3__120__throw_length_errorB8ue170006EPKc
+ __ZNSt3__125__throw_bad_function_callB8ue170006Ev
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_10shared_ptrI8PKCFieldEEEENS_16reverse_iteratorIPS5_EEEEED2B8ue170006Ev
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_8weak_ptrI8PKCFieldEEEENS_16reverse_iteratorIPS5_EEEEED2B8ue170006Ev
+ __ZNSt3__142__uninitialized_allocator_move_if_noexceptB8ue170006INS_9allocatorINS_10shared_ptrI8PKCFieldEEEENS_16reverse_iteratorIPS4_EES8_S8_EET2_RT_T0_T1_S9_
+ __ZNSt3__142__uninitialized_allocator_move_if_noexceptB8ue170006INS_9allocatorINS_8weak_ptrI8PKCFieldEEEENS_16reverse_iteratorIPS4_EES8_S8_EET2_RT_T0_T1_S9_
+ __ZNSt3__16vectorI6b2Vec2NS_9allocatorIS1_EEE11__vallocateB8ue170006Em
+ __ZNSt3__16vectorI6b2Vec2NS_9allocatorIS1_EEE18__assign_with_sizeB8ue170006IPS1_S6_EEvT_T0_l
+ __ZNSt3__16vectorI7CGPointNS_9allocatorIS1_EEE11__vallocateB8ue170006Em
+ __ZNSt3__16vectorI7CGPointNS_9allocatorIS1_EEE16__init_with_sizeB8ue170006IPS1_S6_EEvT_T0_m
+ __ZNSt3__16vectorI7CGPointNS_9allocatorIS1_EEE18__insert_with_sizeB8ue170006INS_11__wrap_iterIPKS1_EES9_EENS6_IPS1_EES9_T_T0_l
+ __ZNSt3__16vectorI7CGPointNS_9allocatorIS1_EEE18__insert_with_sizeB8ue170006INS_11__wrap_iterIPS1_EES8_EES8_NS6_IPKS1_EET_T0_l
+ __ZNSt3__16vectorI7PKPointNS_9allocatorIS1_EEE11__vallocateB8ue170006Em
+ __ZNSt3__16vectorI7PKPointNS_9allocatorIS1_EEE16__init_with_sizeB8ue170006IPS1_S6_EEvT_T0_m
+ __ZNSt3__16vectorI7PKPointNS_9allocatorIS1_EEE18__assign_with_sizeB8ue170006IPS1_S6_EEvT_T0_l
+ __ZNSt3__16vectorI7PKPointNS_9allocatorIS1_EEE18__insert_with_sizeB8ue170006INS_11__wrap_iterIPKS1_EES9_EENS6_IPS1_EES9_T_T0_l
+ __ZNSt3__16vectorI7PKPointNS_9allocatorIS1_EEE18__insert_with_sizeB8ue170006INS_11__wrap_iterIPS1_EES8_EES8_NS6_IPKS1_EET_T0_l
+ __ZNSt3__16vectorI7PKPointNS_9allocatorIS1_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS1_RS3_EEPS1_
+ __ZNSt3__16vectorIDv2_fNS_9allocatorIS1_EEE11__vallocateB8ue170006Em
+ __ZNSt3__16vectorIDv2_fNS_9allocatorIS1_EEE16__init_with_sizeB8ue170006IPS1_S6_EEvT_T0_m
+ __ZNSt3__16vectorINS_10shared_ptrI8PKCFieldEENS_9allocatorIS3_EEE16__destroy_vectorclB8ue170006Ev
+ __ZNSt3__16vectorINS_10shared_ptrI8PKCFieldEENS_9allocatorIS3_EEE7__clearB8ue170006Ev
+ __ZNSt3__16vectorINS_10shared_ptrI8PKCFieldEENS_9allocatorIS3_EEE9push_backB8ue170006ERKS3_
+ __ZNSt3__16vectorINS_8weak_ptrI8PKCFieldEENS_9allocatorIS3_EEE16__destroy_vectorclB8ue170006Ev
+ __ZNSt3__16vectorINS_8weak_ptrI8PKCFieldEENS_9allocatorIS3_EEE7__clearB8ue170006Ev
+ __ZNSt3__16vectorINS_8weak_ptrI8PKCFieldEENS_9allocatorIS3_EEE9push_backB8ue170006ERKS3_
+ __ZSt28__throw_bad_array_new_lengthB8ue170006v
+ ___assert_rtn
- GCC_except_table101
- GCC_except_table120
- GCC_except_table126
- GCC_except_table134
- GCC_except_table135
- GCC_except_table139
- GCC_except_table150
- GCC_except_table159
- GCC_except_table165
- GCC_except_table27
- __ZGVZN16b2ContactManagerC1EvE18b2_defaultListener
- __ZNKSt3__111__move_loopINS_17_ClassicAlgPolicyEEclB7v160006IPNS_8weak_ptrI8PKCFieldEES7_S7_EENS_4pairIT_T1_EES9_T0_SA_
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorINS_10shared_ptrI8PKCFieldEEEENS_16reverse_iteratorIPS4_EEEclB7v160006Ev
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorINS_8weak_ptrI8PKCFieldEEEENS_16reverse_iteratorIPS4_EEEclB7v160006Ev
- __ZNKSt3__16vectorI14b2FixtureProxyNS_9allocatorIS1_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorI6b2Vec2NS_9allocatorIS1_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorI7CGPointNS_9allocatorIS1_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorI7PKPointNS_9allocatorIS1_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIDv2_fNS_9allocatorIS1_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIDv4_fNS_9allocatorIS1_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIN17PKDebugDrawPacket6color4ENS_9allocatorIS2_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorINS_10shared_ptrI8PKCFieldEENS_9allocatorIS3_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorINS_8weak_ptrI8PKCFieldEENS_9allocatorIS3_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIP12QuadTreeNodeNS_9allocatorIS2_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIP14PKPhysicsShapeNS_9allocatorIS2_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIP6b2BodyNS_9allocatorIS2_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIP7b2JointNS_9allocatorIS2_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIP8PKCFieldNS_9allocatorIS2_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIP8QuadTreeNS_9allocatorIS2_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIP9b2ContactNS_9allocatorIS2_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIaNS_9allocatorIaEEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB7v160006Ev
- __ZNKSt9type_infoeqB7v160006ERKS_
- __ZNSt12length_errorC1B7v160006EPKc
- __ZNSt3__110__function12__value_funcIFvffiEEC2B7v160006ERKS3_
- __ZNSt3__110__function12__value_funcIFvffiEED2B7v160006Ev
- __ZNSt3__110shared_ptrI6PKPathEC2IS1_vEEPT_
- __ZNSt3__114__split_bufferINS_10shared_ptrI8PKCFieldEERNS_9allocatorIS3_EEE5clearB7v160006Ev
- __ZNSt3__114__split_bufferINS_8weak_ptrI8PKCFieldEERNS_9allocatorIS3_EEE5clearB7v160006Ev
- __ZNSt3__115allocate_sharedB7v160006I12PKCFieldDragNS_9allocatorIS1_EEJEvEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB7v160006I12PKCFieldUserNS_9allocatorIS1_EEJPvEvEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB7v160006I13PKCFieldNoiseNS_9allocatorIS1_EEJEvEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB7v160006I14PKCFieldSpringNS_9allocatorIS1_EEJEvEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB7v160006I14PKCFieldVortexNS_9allocatorIS1_EEJEvEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB7v160006I16PKCFieldElectricNS_9allocatorIS1_EEJEvEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB7v160006I16PKCFieldMagneticNS_9allocatorIS1_EEJEvEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB7v160006I16PKCFieldVelocityNS_9allocatorIS1_EEJEvEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB7v160006I18PKCFieldTurbulenceNS_9allocatorIS1_EEJEvEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB7v160006I21PKCFieldLinearGravityNS_9allocatorIS1_EEJEvEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB7v160006I21PKCFieldRadialGravityNS_9allocatorIS1_EEJEvEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB7v160006I6PKPathNS_9allocatorIS1_EEJRS1_EvEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB7v160006I7PKCGridNS_9allocatorIS1_EEJEvEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB7v160006I8QuadTreeNS_9allocatorIS1_EEJfffffEvEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorI14b2FixtureProxyEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorI6b2Vec2EEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorI7CGPointEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorI7PKPointEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIDv2_fEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIDv4_fEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIN17PKDebugDrawPacket6color4EEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorINS_10shared_ptrI8PKCFieldEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorINS_8weak_ptrI8PKCFieldEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIP12QuadTreeNodeEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIP14PKPhysicsShapeEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIP6b2BodyEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIP7b2JointEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIP8PKCFieldEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIP8QuadTreeEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIP9b2ContactEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__shared_weak_count16__release_sharedB7v160006Ev
- __ZNSt3__120__shared_ptr_emplaceI12PKCFieldDragNS_9allocatorIS1_EEEC2B7v160006IJEEES3_DpOT_
- __ZNSt3__120__shared_ptr_emplaceI12PKCFieldUserNS_9allocatorIS1_EEEC2B7v160006IJPvEEES3_DpOT_
- __ZNSt3__120__shared_ptr_emplaceI13PKCFieldNoiseNS_9allocatorIS1_EEEC2B7v160006IJEEES3_DpOT_
- __ZNSt3__120__shared_ptr_emplaceI14PKCFieldSpringNS_9allocatorIS1_EEEC2B7v160006IJEEES3_DpOT_
- __ZNSt3__120__shared_ptr_emplaceI14PKCFieldVortexNS_9allocatorIS1_EEEC2B7v160006IJEEES3_DpOT_
- __ZNSt3__120__shared_ptr_emplaceI16PKCFieldElectricNS_9allocatorIS1_EEEC2B7v160006IJEEES3_DpOT_
- __ZNSt3__120__shared_ptr_emplaceI16PKCFieldMagneticNS_9allocatorIS1_EEEC2B7v160006IJEEES3_DpOT_
- __ZNSt3__120__shared_ptr_emplaceI16PKCFieldVelocityNS_9allocatorIS1_EEEC2B7v160006IJEEES3_DpOT_
- __ZNSt3__120__shared_ptr_emplaceI18PKCFieldTurbulenceNS_9allocatorIS1_EEEC2B7v160006IJEEES3_DpOT_
- __ZNSt3__120__shared_ptr_emplaceI21PKCFieldLinearGravityNS_9allocatorIS1_EEEC2B7v160006IJEEES3_DpOT_
- __ZNSt3__120__shared_ptr_emplaceI21PKCFieldRadialGravityNS_9allocatorIS1_EEEC2B7v160006IJEEES3_DpOT_
- __ZNSt3__120__shared_ptr_emplaceI6PKPathNS_9allocatorIS1_EEEC2B7v160006IJRS1_EEES3_DpOT_
- __ZNSt3__120__shared_ptr_emplaceI7PKCGridNS_9allocatorIS1_EEEC2B7v160006IJEEES3_DpOT_
- __ZNSt3__120__shared_ptr_emplaceI8QuadTreeNS_9allocatorIS1_EEEC2B7v160006IJfffffEEES3_DpOT_
- __ZNSt3__120__throw_length_errorB7v160006EPKc
- __ZNSt3__125__throw_bad_function_callB7v160006Ev
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_10shared_ptrI8PKCFieldEEEENS_16reverse_iteratorIPS5_EEEEED2B7v160006Ev
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_8weak_ptrI8PKCFieldEEEENS_16reverse_iteratorIPS5_EEEEED2B7v160006Ev
- __ZNSt3__142__uninitialized_allocator_move_if_noexceptB7v160006INS_9allocatorINS_10shared_ptrI8PKCFieldEEEENS_16reverse_iteratorIPS4_EES8_S8_EET2_RT_T0_T1_S9_
- __ZNSt3__142__uninitialized_allocator_move_if_noexceptB7v160006INS_9allocatorINS_8weak_ptrI8PKCFieldEEEENS_16reverse_iteratorIPS4_EES8_S8_EET2_RT_T0_T1_S9_
- __ZNSt3__16vectorI6b2Vec2NS_9allocatorIS1_EEE11__vallocateB7v160006Em
- __ZNSt3__16vectorI6b2Vec2NS_9allocatorIS1_EEE6assignIPS1_Li0EEEvT_S7_
- __ZNSt3__16vectorI7CGPointNS_9allocatorIS1_EEE11__vallocateB7v160006Em
- __ZNSt3__16vectorI7CGPointNS_9allocatorIS1_EEE6insertINS_11__wrap_iterIPKS1_EELi0EEENS6_IPS1_EES9_T_SC_
- __ZNSt3__16vectorI7CGPointNS_9allocatorIS1_EEE6insertINS_11__wrap_iterIPS1_EELi0EEES8_NS6_IPKS1_EET_SC_
- __ZNSt3__16vectorI7CGPointNS_9allocatorIS1_EEEC2ERKS4_
- __ZNSt3__16vectorI7PKPointNS_9allocatorIS1_EEE11__vallocateB7v160006Em
- __ZNSt3__16vectorI7PKPointNS_9allocatorIS1_EEE6assignIPS1_Li0EEEvT_S7_
- __ZNSt3__16vectorI7PKPointNS_9allocatorIS1_EEE6insertINS_11__wrap_iterIPKS1_EELi0EEENS6_IPS1_EES9_T_SC_
- __ZNSt3__16vectorI7PKPointNS_9allocatorIS1_EEE6insertINS_11__wrap_iterIPS1_EELi0EEES8_NS6_IPKS1_EET_SC_
- __ZNSt3__16vectorI7PKPointNS_9allocatorIS1_EEEC2ERKS4_
- __ZNSt3__16vectorIDv2_fNS_9allocatorIS1_EEE11__vallocateB7v160006Em
- __ZNSt3__16vectorIDv2_fNS_9allocatorIS1_EEEC2ERKS4_
- __ZNSt3__16vectorINS_10shared_ptrI8PKCFieldEENS_9allocatorIS3_EEE16__destroy_vectorclB7v160006Ev
- __ZNSt3__16vectorINS_10shared_ptrI8PKCFieldEENS_9allocatorIS3_EEE7__clearB7v160006Ev
- __ZNSt3__16vectorINS_10shared_ptrI8PKCFieldEENS_9allocatorIS3_EEE9push_backB7v160006ERKS3_
- __ZNSt3__16vectorINS_10shared_ptrI8PKCFieldEENS_9allocatorIS3_EEED2B7v160006Ev
- __ZNSt3__16vectorINS_8weak_ptrI8PKCFieldEENS_9allocatorIS3_EEE16__destroy_vectorclB7v160006Ev
- __ZNSt3__16vectorINS_8weak_ptrI8PKCFieldEENS_9allocatorIS3_EEE7__clearB7v160006Ev
- __ZNSt3__16vectorINS_8weak_ptrI8PKCFieldEENS_9allocatorIS3_EEE9push_backB7v160006ERKS3_
- __ZNSt3__16vectorINS_8weak_ptrI8PKCFieldEENS_9allocatorIS3_EEED2B7v160006Ev
- __ZSt28__throw_bad_array_new_lengthB7v160006v
- ___cxa_atexit
CStrings:
+ "-[PKPhysicsBody copyWithZone:]"
+ "0 < count && count < 3"
+ "0 < m_nodeCount"
+ "0 <= child1 && child1 < m_nodeCapacity"
+ "0 <= child2 && child2 < m_nodeCapacity"
+ "0 <= childIndex && childIndex < m_proxies.size()"
+ "0 <= edge1 && edge1 < poly1->GetVertexCount()"
+ "0 <= freeIndex && freeIndex < m_nodeCapacity"
+ "0 <= iB && iB < m_nodeCapacity"
+ "0 <= iC && iC < m_nodeCapacity"
+ "0 <= iD && iD < m_nodeCapacity"
+ "0 <= iE && iE < m_nodeCapacity"
+ "0 <= iF && iF < m_nodeCapacity"
+ "0 <= iG && iG < m_nodeCapacity"
+ "0 <= index && index < GetVertexCount()"
+ "0 <= index && index < GetVertexCount() - 1"
+ "0 <= index && index < chain->GetVertexCount()"
+ "0 <= index && index < m_vertices.size()"
+ "0 <= nodeId && nodeId < m_nodeCapacity"
+ "0 <= proxyId && proxyId < m_nodeCapacity"
+ "0 <= type1 && type1 < b2Shape::e_typeCount"
+ "0 <= type2 && type2 < b2Shape::e_typeCount"
+ "0.0f <= lower && lower <= input.maxFraction"
+ "AddType"
+ "Allocate"
+ "AllocateNode"
+ "Balance"
+ "ComputeAABB"
+ "ComputeCentroid"
+ "ComputeHeight"
+ "ComputeMass"
+ "Create"
+ "CreateBody"
+ "CreateChain"
+ "CreateFixture"
+ "CreateJoint"
+ "Destroy"
+ "DestroyBody"
+ "DestroyFixture"
+ "DestroyJoint"
+ "DestroyProxy"
+ "Evaluate"
+ "FindMinSeparation"
+ "FindMinimumTOI"
+ "Free"
+ "FreeNode"
+ "GetAABB"
+ "GetCategoryBits"
+ "GetChildEdge"
+ "GetClosestPoint"
+ "GetCollisionBits"
+ "GetFatAABB"
+ "GetFixtureProxy"
+ "GetHeight() == ComputeHeight()"
+ "GetMaxBalance"
+ "GetMetric"
+ "GetSearchDirection"
+ "GetVertex"
+ "GetVertexCount() >= 3"
+ "GetWitnessPoints"
+ "InitVelocityConstraints"
+ "Initialize"
+ "InitializeVelocityConstraints"
+ "InsertLeaf"
+ "IsLocked() == false"
+ "MoveProxy"
+ "PKPhysicsBody.mm"
+ "RayCast"
+ "ReadCache"
+ "Set"
+ "SetActive"
+ "SetDensity"
+ "SetLimits"
+ "SetMassData"
+ "SetMaxForce"
+ "SetMaxTorque"
+ "SetRatio"
+ "SetTransform"
+ "SetType"
+ "SolveTOI"
+ "SolveVelocityConstraints"
+ "Validate"
+ "ValidateMetrics"
+ "ValidateStructure"
+ "a.x >= 0.0f && a.y >= 0.0f"
+ "aabb.lowerBound == node->aabb.lowerBound"
+ "aabb.upperBound == node->aabb.upperBound"
+ "alpha0 < 1.0f"
+ "b2Body"
+ "b2Body.mm"
+ "b2ChainAndCircleContact"
+ "b2ChainAndCircleContact.cpp"
+ "b2ChainAndPolygonContact"
+ "b2ChainAndPolygonContact.cpp"
+ "b2ChainShape.cpp"
+ "b2ChainShape.h"
+ "b2CircleContact"
+ "b2CircleContact.cpp"
+ "b2CollideEdge.cpp"
+ "b2CollideEdgeAndCircle"
+ "b2CollidePolygon.cpp"
+ "b2Contact.cpp"
+ "b2ContactManager.cpp"
+ "b2ContactSolver"
+ "b2ContactSolver.cpp"
+ "b2Distance"
+ "b2Distance.cpp"
+ "b2Distance.h"
+ "b2DynamicTree.cpp"
+ "b2DynamicTree.h"
+ "b2EdgeAndCircleContact"
+ "b2EdgeAndCircleContact.cpp"
+ "b2EdgeAndPolygonContact"
+ "b2EdgeAndPolygonContact.cpp"
+ "b2EdgeSeparation"
+ "b2FindIncidentEdge"
+ "b2Fixture.h"
+ "b2FrictionJoint.cpp"
+ "b2GearJoint"
+ "b2GearJoint.cpp"
+ "b2IsValid(bd->angle)"
+ "b2IsValid(bd->angularDamping) && bd->angularDamping >= 0.0f"
+ "b2IsValid(bd->angularVelocity)"
+ "b2IsValid(bd->linearDamping) && bd->linearDamping >= 0.0f"
+ "b2IsValid(def->dampingRatio) && def->dampingRatio >= 0.0f"
+ "b2IsValid(def->frequencyHz) && def->frequencyHz >= 0.0f"
+ "b2IsValid(def->maxForce) && def->maxForce >= 0.0f"
+ "b2IsValid(density) && density >= 0.0f"
+ "b2IsValid(force) && force >= 0.0f"
+ "b2IsValid(ratio)"
+ "b2IsValid(torque) && torque >= 0.0f"
+ "b2Island.mm"
+ "b2Joint"
+ "b2Joint.cpp"
+ "b2MouseJoint"
+ "b2MouseJoint.cpp"
+ "b2PolygonAndCircleContact"
+ "b2PolygonAndCircleContact.cpp"
+ "b2PolygonContact"
+ "b2PolygonContact.cpp"
+ "b2PolygonShape.cpp"
+ "b2PolygonShape.h"
+ "b2PrismaticJoint.cpp"
+ "b2PulleyJoint"
+ "b2PulleyJoint.cpp"
+ "b2QuadtreeAndCircleContact"
+ "b2QuadtreeAndOtherContact.cpp"
+ "b2RevoluteJoint.cpp"
+ "b2Rope.cpp"
+ "b2StackAllocator.cpp"
+ "b2TimeOfImpact"
+ "b2TimeOfImpact.cpp"
+ "b2World.mm"
+ "bd->linearVelocity.IsValid()"
+ "bd->position.IsValid()"
+ "cache->count <= 3"
+ "child1 != (-1)"
+ "child2 != (-1)"
+ "child2 == (-1)"
+ "childIndex < GetVertexCount()"
+ "count >= 2"
+ "count >= 3"
+ "d + h * k > 1.19209290e-7F"
+ "def->bodyA != def->bodyB"
+ "def->count >= 3"
+ "def->ratio != 0.0f"
+ "def->target.IsValid()"
+ "den > 0.0f"
+ "false"
+ "fixture->m_body == this"
+ "found"
+ "iA != (-1)"
+ "lower <= upper"
+ "m_I > 0.0f"
+ "m_bodyCount > 0"
+ "m_entryCount < b2_maxStackEntries"
+ "m_entryCount == 0"
+ "m_entryCount > 0"
+ "m_fixtureA->GetType() == b2Shape::e_chain"
+ "m_fixtureA->GetType() == b2Shape::e_circle"
+ "m_fixtureA->GetType() == b2Shape::e_edge"
+ "m_fixtureA->GetType() == b2Shape::e_polygon"
+ "m_fixtureA->GetType() == b2Shape::e_quadtree"
+ "m_fixtureB->GetType() == b2Shape::e_chain"
+ "m_fixtureB->GetType() == b2Shape::e_circle"
+ "m_fixtureB->GetType() == b2Shape::e_edge"
+ "m_fixtureB->GetType() == b2Shape::e_polygon"
+ "m_fixtureB->GetType() == b2Shape::e_quadtree"
+ "m_fixtureCount > 0"
+ "m_index == 0"
+ "m_jointCount > 0"
+ "m_nodeCount + freeCount == m_nodeCapacity"
+ "m_nodeCount == m_nodeCapacity"
+ "m_nodes[B->parent].child2 == iA"
+ "m_nodes[C->parent].child2 == iA"
+ "m_nodes[child1].parent == index"
+ "m_nodes[child2].parent == index"
+ "m_nodes[index].parent == (-1)"
+ "m_nodes[proxyId].IsLeaf()"
+ "m_typeA == e_revoluteJoint || m_typeA == e_prismaticJoint"
+ "m_typeB == e_revoluteJoint || m_typeB == e_prismaticJoint"
+ "m_world->IsLocked() == false"
+ "manifold->pointCount > 0"
+ "node->IsLeaf() == false"
+ "node->height == 0"
+ "node->height == height"
+ "p == entry->data"
+ "pc->pointCount > 0"
+ "pointCount > 0"
+ "r.LengthSquared() > 0.0f"
+ "ratio > 1.19209290e-7F"
+ "s_initialized == true"
+ "target > tolerance"
+ "toiIndexA < bodyCount"
+ "toiIndexB < bodyCount"
+ "~b2StackAllocator"

```
