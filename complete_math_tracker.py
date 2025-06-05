#!/usr/bin/env python3
"""
Complete Mathematics Mastery Tracker
Handles 9 phases from high school through research-level mathematics
"""

import json
import datetime
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

@dataclass
class MathConcept:
    """Represents a mathematical concept with mastery tracking"""
    name: str
    phase: int
    module: str
    difficulty: int  # 1-10 scale
    prerequisites: List[str]
    mastery_level: int  # 0-5 scale
    time_invested: int  # minutes
    last_reviewed: Optional[str] = None
    
@dataclass
class ResearchProject:
    """Track research projects and publications"""
    title: str
    phase: int
    start_date: str
    status: str  # "planning", "active", "completed", "published"
    collaborators: List[str]
    abstract: str
    milestones: List[Dict]
    publications: List[str]

@dataclass
class CareerGoal:
    """Track career-related goals and milestones"""
    goal_type: str  # "academic", "industry", "consulting", "tech"
    target_position: str
    timeline: str
    required_phases: List[int]
    current_progress: float  # 0-1
    action_items: List[str]

class CompleteMathTracker:
    """Comprehensive tracking system for complete mathematics mastery"""
    
    def __init__(self, data_file: str = "complete_math_data.json"):
        self.data_file = Path(data_file)
        self.data = self._load_data()
        self.phases = self._initialize_phases()
    
    def _initialize_phases(self) -> Dict:
        """Initialize the complete phase structure"""
        return {
            1: {
                "name": "Foundation (Matematik 5000 4&5)",
                "duration_weeks": 14,
                "level": "Advanced High School → Early College",
                "modules": [
                    "Complex Numbers & Advanced Algebra",
                    "Sequences & Series", 
                    "Differential & Integral Calculus",
                    "Differential Equations",
                    "Linear Algebra Fundamentals",
                    "Vector Calculus & Statistics"
                ]
            },
            2: {
                "name": "Undergraduate Core Mathematics", 
                "duration_months": 20,
                "level": "College Sophomore → Junior",
                "modules": [
                    "Advanced Calculus & Real Analysis",
                    "Abstract Algebra",
                    "Advanced Linear Algebra", 
                    "Discrete Mathematics & Combinatorics",
                    "Ordinary Differential Equations (Advanced)",
                    "Probability Theory & Statistics",
                    "Mathematical Logic & Set Theory",
                    "Introduction to Topology",
                    "Complex Analysis",
                    "Numerical Analysis"
                ]
            },
            3: {
                "name": "Advanced Undergraduate",
                "duration_months": 12, 
                "level": "Senior Undergraduate → Graduate Preparation",
                "modules": [
                    "Advanced Real Analysis",
                    "Advanced Abstract Algebra",
                    "Differential Geometry",
                    "Algebraic Topology", 
                    "Partial Differential Equations",
                    "Mathematical Physics"
                ]
            },
            4: {
                "name": "Graduate Foundations",
                "duration_months": 24,
                "level": "First-Year Graduate",
                "modules": [
                    "Advanced Functional Analysis",
                    "Algebraic Geometry",
                    "Number Theory (Advanced)",
                    "Representation Theory",
                    "Advanced Topology",
                    "Advanced Probability",
                    "Advanced Differential Equations",
                    "Mathematical Logic (Advanced)"
                ]
            },
            5: {
                "name": "Advanced Graduate",
                "duration_months": 12,
                "level": "Advanced Graduate → PhD Candidacy", 
                "modules": [
                    "Research Area Specialization",
                    "Advanced Research Methods"
                ]
            },
            6: {
                "name": "Research Preparation",
                "duration_months": 12,
                "level": "PhD Research Preparation",
                "modules": [
                    "Literature Mastery",
                    "Research Problem Identification", 
                    "Advanced Seminar Participation",
                    "Qualifying Examination Preparation"
                ]
            },
            7: {
                "name": "Specialized Research Tracks",
                "duration_months": 12,
                "level": "Advanced PhD Research",
                "modules": [
                    "Pure Mathematics Research Frontiers",
                    "Applied Mathematics Research Frontiers",
                    "Computational & Data Science"
                ]
            },
            8: {
                "name": "Cutting-Edge Research Topics", 
                "duration_months": 12,
                "level": "Research Leadership",
                "modules": [
                    "Emerging Mathematical Fields",
                    "Advanced Research Methodologies",
                    "Mathematical Innovation",
                    "Research Impact & Legacy"
                ]
            },
            9: {
                "name": "Mathematical Frontiers & Beyond",
                "duration_months": "Ongoing",
                "level": "Research Pioneer",
                "modules": [
                    "Unsolved Problems & Grand Challenges",
                    "Future Mathematics"
                ]
            }
        }
    
    def _load_data(self) -> Dict:
        """Load existing data or create new structure"""
        if self.data_file.exists():
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return {
            "concepts": {},
            "research_projects": [],
            "career_goals": [],
            "phase_progress": {str(i): 0.0 for i in range(1, 10)},
            "learning_analytics": {},
            "milestones": [],
            "study_sessions": [],
            "spaced_repetition": {},
            "skill_assessments": {},
            "networking_contacts": [],
            "publications": [],
            "awards": [],
            "conference_presentations": []
        }
    
    def add_concept(self, concept: MathConcept):
        """Add a new mathematical concept to track"""
        concept_dict = asdict(concept)
        self.data["concepts"][concept.name] = concept_dict
        self.save_data()
    
    def update_mastery(self, concept_name: str, new_level: int, time_spent: int):
        """Update mastery level for a concept"""
        if concept_name in self.data["concepts"]:
            self.data["concepts"][concept_name]["mastery_level"] = new_level
            self.data["concepts"][concept_name]["time_invested"] += time_spent
            self.data["concepts"][concept_name]["last_reviewed"] = datetime.date.today().isoformat()
            self._update_phase_progress()
            self.save_data()
    
    def _update_phase_progress(self):
        """Calculate progress for each phase based on concept mastery"""
        for phase_num in range(1, 10):
            phase_concepts = [
                c for c in self.data["concepts"].values() 
                if c["phase"] == phase_num
            ]
            if phase_concepts:
                total_mastery = sum(c["mastery_level"] for c in phase_concepts)
                max_possible = len(phase_concepts) * 5  # Max mastery level is 5
                progress = total_mastery / max_possible if max_possible > 0 else 0
                self.data["phase_progress"][str(phase_num)] = progress
    
    def add_research_project(self, project: ResearchProject):
        """Add a research project"""
        project_dict = asdict(project)
        self.data["research_projects"].append(project_dict)
        self.save_data()
    
    def add_career_goal(self, goal: CareerGoal):
        """Add a career goal"""
        goal_dict = asdict(goal)
        self.data["career_goals"].append(goal_dict)
        self.save_data()
    
    def get_current_recommendations(self) -> Dict:
        """Get personalized recommendations based on current progress"""
        recommendations = {
            "next_concepts": [],
            "review_needed": [],
            "phase_focus": None,
            "career_actions": [],
            "research_opportunities": []
        }
        
        # Find current phase
        current_phase = 1
        for phase_num in range(1, 10):
            if self.data["phase_progress"][str(phase_num)] < 0.8:  # 80% mastery threshold
                current_phase = phase_num
                break
        
        recommendations["phase_focus"] = f"Phase {current_phase}: {self.phases[current_phase]['name']}"
        
        # Find concepts needing review (not reviewed in last 30 days)
        thirty_days_ago = (datetime.date.today() - datetime.timedelta(days=30)).isoformat()
        for concept_name, concept in self.data["concepts"].items():
            if concept.get("last_reviewed", "1900-01-01") < thirty_days_ago:
                recommendations["review_needed"].append(concept_name)
        
        # Find next concepts to learn
        mastered_concepts = [
            name for name, concept in self.data["concepts"].items()
            if concept["mastery_level"] >= 4  # Consider 4+ as mastered
        ]
        
        for concept_name, concept in self.data["concepts"].items():
            if (concept["mastery_level"] < 4 and 
                all(prereq in mastered_concepts for prereq in concept["prerequisites"])):
                recommendations["next_concepts"].append(concept_name)
        
        return recommendations
    
    def generate_learning_path(self, career_goal: str, timeline_years: int) -> Dict:
        """Generate a personalized learning path based on career goals"""
        career_paths = {
            "academic": {
                "required_phases": [1, 2, 3, 4, 5, 6, 7, 8],
                "emphasis": ["theoretical_depth", "research_skills", "publication"],
                "timeline_multiplier": 1.2  # Academic path takes longer
            },
            "industry": {
                "required_phases": [1, 2, 3, 4, 5, 6],
                "emphasis": ["applied_skills", "computational", "collaboration"],
                "timeline_multiplier": 0.8  # Industry path can be faster
            },
            "consulting": {
                "required_phases": [1, 2, 3, 4, 5],
                "emphasis": ["broad_knowledge", "communication", "problem_solving"],
                "timeline_multiplier": 0.7
            },
            "tech": {
                "required_phases": [1, 2, 3, 4, 5, 7],  # Skip some pure math, focus on computational
                "emphasis": ["programming", "algorithms", "machine_learning"],
                "timeline_multiplier": 0.6
            }
        }
        
        if career_goal not in career_paths:
            return {"error": "Invalid career goal"}
        
        path = career_paths[career_goal]
        adjusted_timeline = timeline_years * path["timeline_multiplier"]
        
        # Calculate time allocation for each phase
        total_months = sum(
            self.phases[phase]["duration_months"] if isinstance(self.phases[phase]["duration_months"], int) 
            else 12  # Default for ongoing phases
            for phase in path["required_phases"]
        )
        
        time_allocation = {}
        for phase in path["required_phases"]:
            phase_months = (self.phases[phase]["duration_months"] 
                          if isinstance(self.phases[phase]["duration_months"], int) else 12)
            allocated_time = (phase_months / total_months) * (adjusted_timeline * 12)
            time_allocation[phase] = allocated_time
        
        return {
            "career_goal": career_goal,
            "timeline_years": adjusted_timeline,
            "required_phases": path["required_phases"],
            "emphasis_areas": path["emphasis"],
            "time_allocation": time_allocation,
            "milestones": self._generate_milestones(path["required_phases"], adjusted_timeline)
        }
    
    def _generate_milestones(self, phases: List[int], timeline_years: float) -> List[Dict]:
        """Generate milestone timeline for career path"""
        milestones = []
        cumulative_time = 0
        
        for phase in phases:
            phase_info = self.phases[phase]
            phase_duration = (phase_info["duration_months"] 
                            if isinstance(phase_info["duration_months"], int) else 12)
            
            cumulative_time += phase_duration
            milestone_date = datetime.date.today() + datetime.timedelta(days=cumulative_time * 30)
            
            milestones.append({
                "phase": phase,
                "name": phase_info["name"],
                "target_date": milestone_date.isoformat(),
                "level": phase_info["level"],
                "key_skills": phase_info["modules"][:3]  # Top 3 modules
            })
        
        return milestones
    
    def generate_comprehensive_report(self) -> Dict:
        """Generate a comprehensive progress report"""
        total_concepts = len(self.data["concepts"])
        mastered_concepts = sum(1 for c in self.data["concepts"].values() if c["mastery_level"] >= 4)
        
        total_time = sum(c["time_invested"] for c in self.data["concepts"].values())
        
        phase_progress = {
            int(k): v for k, v in self.data["phase_progress"].items()
        }
        
        current_phase = max(k for k, v in phase_progress.items() if v > 0.1)
        
        return {
            "overall_progress": {
                "concepts_mastered": f"{mastered_concepts}/{total_concepts}",
                "mastery_percentage": (mastered_concepts / total_concepts * 100) if total_concepts > 0 else 0,
                "total_study_time_hours": total_time / 60,
                "current_phase": current_phase,
                "current_level": self.phases[current_phase]["level"]
            },
            "phase_breakdown": {
                phase: {
                    "progress": progress * 100,
                    "status": "Completed" if progress >= 0.9 else "In Progress" if progress > 0 else "Not Started"
                }
                for phase, progress in phase_progress.items()
            },
            "research_activity": {
                "active_projects": len([p for p in self.data["research_projects"] if p["status"] == "active"]),
                "completed_projects": len([p for p in self.data["research_projects"] if p["status"] == "completed"]),
                "publications": len(self.data["publications"])
            },
            "career_progress": {
                "defined_goals": len(self.data["career_goals"]),
                "networking_contacts": len(self.data["networking_contacts"]),
                "presentations": len(self.data["conference_presentations"]),
                "awards": len(self.data["awards"])
            },
            "recommendations": self.get_current_recommendations()
        }
    
    def visualize_progress(self, save_path: str = "math_progress.png"):
        """Create a visual progress chart"""
        phases = list(range(1, 10))
        progress = [self.data["phase_progress"][str(p)] * 100 for p in phases]
        phase_names = [self.phases[p]["name"][:20] + "..." if len(self.phases[p]["name"]) > 20 
                      else self.phases[p]["name"] for p in phases]
        
        plt.figure(figsize=(15, 8))
        bars = plt.bar(phases, progress, color=['green' if p >= 90 else 'orange' if p >= 50 else 'red' for p in progress])
        
        plt.xlabel('Phase')
        plt.ylabel('Progress (%)')
        plt.title('Complete Mathematics Mastery Progress')
        plt.xticks(phases, [f"P{p}" for p in phases], rotation=45)
        
        # Add phase names as labels
        for i, (bar, name) in enumerate(zip(bars, phase_names)):
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height + 1,
                    f"{height:.1f}%\n{name}", ha='center', va='bottom', fontsize=8, rotation=45)
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
    
    def save_data(self):
        """Save data to JSON file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=2)

# Example CLI interface
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Complete Mathematics Mastery Tracker")
    parser.add_argument("--report", action="store_true", help="Generate comprehensive report")
    parser.add_argument("--path", type=str, help="Generate learning path for career goal")
    parser.add_argument("--timeline", type=int, default=8, help="Timeline in years for career path")
    parser.add_argument("--visualize", action="store_true", help="Create progress visualization")
    parser.add_argument("--add-concept", action="store_true", help="Add a new concept")
    parser.add_argument("--update-mastery", nargs=3, help="Update mastery: concept_name new_level time_spent")
    
    args = parser.parse_args()
    tracker = CompleteMathTracker()
    
    if args.report:
        report = tracker.generate_comprehensive_report()
        print("📊 COMPREHENSIVE MATHEMATICS PROGRESS REPORT")
        print("=" * 50)
        
        overall = report["overall_progress"]
        print(f"🎯 Overall Progress:")
        print(f"   Concepts Mastered: {overall['concepts_mastered']}")
        print(f"   Mastery Percentage: {overall['mastery_percentage']:.1f}%")
        print(f"   Total Study Time: {overall['total_study_time_hours']:.1f} hours")
        print(f"   Current Phase: {overall['current_phase']} ({overall['current_level']})")
        
        print(f"\n📈 Phase Breakdown:")
        for phase, info in report["phase_breakdown"].items():
            print(f"   Phase {phase}: {info['progress']:.1f}% ({info['status']})")
        
        research = report["research_activity"]
        print(f"\n🔬 Research Activity:")
        print(f"   Active Projects: {research['active_projects']}")
        print(f"   Completed Projects: {research['completed_projects']}")
        print(f"   Publications: {research['publications']}")
        
        recommendations = report["recommendations"]
        print(f"\n💡 Recommendations:")
        print(f"   Focus on: {recommendations['phase_focus']}")
        if recommendations['next_concepts']:
            print(f"   Next concepts to learn: {', '.join(recommendations['next_concepts'][:3])}")
        if recommendations['review_needed']:
            print(f"   Concepts needing review: {len(recommendations['review_needed'])}")
    
    elif args.path:
        path = tracker.generate_learning_path(args.path.lower(), args.timeline)
        if "error" in path:
            print(f"❌ {path['error']}")
            print("Available career goals: academic, industry, consulting, tech")
        else:
            print(f"🎯 LEARNING PATH: {path['career_goal'].upper()}")
            print(f"Timeline: {path['timeline_years']:.1f} years")
            print(f"Required Phases: {path['required_phases']}")
            print(f"Emphasis Areas: {', '.join(path['emphasis_areas'])}")
            
            print(f"\n📅 Milestones:")
            for milestone in path['milestones']:
                print(f"   {milestone['target_date']}: Complete {milestone['name']}")
    
    elif args.visualize:
        tracker.visualize_progress()
        print("📊 Progress visualization saved as 'math_progress.png'")
    
    elif args.add_concept:
        print("➕ Add New Concept")
        name = input("Concept name: ")
        phase = int(input("Phase (1-9): "))
        module = input("Module: ")
        difficulty = int(input("Difficulty (1-10): "))
        prerequisites = input("Prerequisites (comma-separated): ").split(",")
        prerequisites = [p.strip() for p in prerequisites if p.strip()]
        
        concept = MathConcept(
            name=name, phase=phase, module=module, difficulty=difficulty,
            prerequisites=prerequisites, mastery_level=0, time_invested=0
        )
        tracker.add_concept(concept)
        print(f"✅ Added concept: {name}")
    
    elif args.update_mastery:
        concept_name, new_level, time_spent = args.update_mastery
        tracker.update_mastery(concept_name, int(new_level), int(time_spent))
        print(f"✅ Updated mastery for {concept_name}: Level {new_level}")
    
    else:
        print("🧮 Complete Mathematics Mastery Tracker")
        print("Use --help to see available commands")
        
        # Quick overview
        report = tracker.generate_comprehensive_report()
        overall = report["overall_progress"]
        print(f"\n📊 Quick Overview:")
        print(f"   Progress: {overall['mastery_percentage']:.1f}%")
        print(f"   Current Phase: {overall['current_phase']}")
        print(f"   Study Time: {overall['total_study_time_hours']:.1f} hours")