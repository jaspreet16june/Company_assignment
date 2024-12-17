def allocate_boxes(time, capacity):
    # Define box volumes and costs for each city
    box_data = {
        "Delhi": [
            ("XXL", 320, 282), ("XL", 160, 140), ("L", 80, 77.4), 
            ("M", 40, 45), ("S", 20, 23), ("XS", 10, 12)
        ],
        "Mumbai": [
            ("XXL", 320, 297), ("XL", 160, 130), ("L", 80, 89), 
            ("M", 40, 41.3), ("XS", 10, 14)
        ],
        "Kolkata": [
            ("XL", 160, 118), ("L", 80, 67), ("XS", 10, 11)
        ],
    }
    
    results = []

    for city, boxes in box_data.items():
        # Sort boxes by cost per unit to minimize cost
        boxes.sort(key=lambda x: x[2] / x[1])  # Cost per unit volume
        
        remaining_capacity = capacity
        total_cost = 0
        box_allocation = []
        
        # Allocate boxes greedily
        for name, volume, cost in boxes:
            num_boxes = remaining_capacity // volume  # Max boxes of this type we can use
            if num_boxes > 0:
                total_cost += num_boxes * cost * time  # Update total cost
                box_allocation.append((name, num_boxes))
                remaining_capacity -= num_boxes * volume
            
            if remaining_capacity == 0:
                break
        
        # Handle any remaining capacity with the smallest box
        if remaining_capacity > 0:
            for name, volume, cost in sorted(boxes, key=lambda x: x[1]):
                if volume >= remaining_capacity:
                    total_cost += cost * time
                    box_allocation.append((name, 1))
                    remaining_capacity = 0
                    break
        
        results.append({
            "region": city,
            "total_cost": round(total_cost, 2),
            "boxes": box_allocation
        })

    return {"Output": results}


# Test Cases
def test_allocate_boxes():
    # Test Case 1: Provided example
    result = allocate_boxes(time=1, capacity=1150)
    assert result == {
        "Output": [
            {
                "region": "Delhi",
                "total_cost": 1015.0,
                "boxes": [("XL", 7), ("S", 1), ("XS", 1)]
            },
            {
                "region": "Mumbai",
                "total_cost": 952.0,
                "boxes": [("XL", 7), ("XS", 3)]
            },
            {
                "region": "Kolkata",
                "total_cost": 857.0,
                "boxes": [("XL", 7), ("S", 1), ("XS", 1)]
            },
        ]
    }
    
    # Test Case 2: Smaller capacity
    result = allocate_boxes(time=2, capacity=200)
    assert result == {
        "Output": [
            {
                "region": "Delhi",
                "total_cost": 280.0,
                "boxes": [("XL", 1), ("XS", 4)]
            },
            {
                "region": "Mumbai",
                "total_cost": 288.0,
                "boxes": [("XL", 1), ("XS", 4)]
            },
            {
                "region": "Kolkata",
                "total_cost": 236.0,
                "boxes": [("XL", 1), ("XS", 4)]
            },
        ]
    }
    
    # Test Case 3: Exact capacity match
    result = allocate_boxes(time=1, capacity=320)
    assert result == {
        "Output": [
            {
                "region": "Delhi",
                "total_cost": 282.0,
                "boxes": [("XXL", 1)]
            },
            {
                "region": "Mumbai",
                "total_cost": 297.0,
                "boxes": [("XXL", 1)]
            },
            {
                "region": "Kolkata",
                "total_cost": 236.0,
                "boxes": [("XL", 2)]
            },
        ]
    }
    
    print("All test cases passed!")



time = 1
capacity = 1150
output = allocate_boxes(time, capacity)
print(output)

# Run Tests
test_allocate_boxes()
